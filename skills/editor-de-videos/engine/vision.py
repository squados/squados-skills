"""Local CPU MediaPipe solutions; frozen Apache-2.0 models matched to the installed wheel."""
from pathlib import Path
import hashlib
from .state import read,write
ROOT=Path(__file__).resolve().parents[1]
def caption_zone(faces):
    return 'top' if any(f['y']+f['h']>.72 and f['y']<.86 for f in faces) else 'bottom'
def mask_quality(coverage):return .04<coverage<.93
def model_path(name):
    import mediapipe
    p=ROOT/'assets/models'/name;manifest=read(ROOT/'assets/manifest.json')
    entry=next(x for x in manifest['models'] if x['path']=='models/'+name)
    if hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256']:raise ValueError('Model checksum mismatch')
    runtime=Path(mediapipe.__file__).parent/entry['runtime_path']
    if hashlib.sha256(runtime.read_bytes()).hexdigest()!=entry['sha256']:raise ValueError('Installed MediaPipe model differs from audited model')
    return runtime
def detect_faces(video):
    import cv2,mediapipe as mp
    model_path('face_detection_short_range.tflite')
    cap=cv2.VideoCapture(str(video));fps=cap.get(cv2.CAP_PROP_FPS);total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT));faces=[]
    with mp.solutions.face_detection.FaceDetection(model_selection=0,min_detection_confidence=.55) as detector:
        for frame in range(0,total,max(1,round(fps*2))):
            cap.set(cv2.CAP_PROP_POS_FRAMES,frame);ok,bgr=cap.read()
            if not ok:continue
            result=detector.process(cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB))
            for d in result.detections or []:
                b=d.location_data.relative_bounding_box;faces.append({'time_us':round(frame/fps*1e6),'x':b.xmin,'y':b.ymin,'w':b.width,'h':b.height,'score':d.score[0]})
    cap.release();return faces
def segment_foreground(project):
    import cv2,mediapipe as mp,numpy as np,subprocess
    p=Path(project);plan=read(p/'frame-plan.json');w,h=plan['width'],plan['height'];cap=cv2.VideoCapture(str(p/'assets/aroll.mp4'));fps=cap.get(cv2.CAP_PROP_FPS)
    model_path('selfie_segmentation.tflite')
    output=p/'assets/foreground.webm';log=(p/'segmentation.log').open('w')
    process=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgba','-s',f'{w}x{h}','-r',str(fps),'-i','pipe:0','-c:v','libvpx-vp9','-pix_fmt','yuva420p','-auto-alt-ref','0','-crf','32','-b:v','0',str(output)],stdin=subprocess.PIPE,stderr=log)
    valid=0;frames=0
    try:
        with mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=0) as segmenter:
            while True:
                ok,bgr=cap.read()
                if not ok:break
                rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB);result=segmenter.process(rgb)
                mask=result.segmentation_mask;mask=cv2.resize(mask,(w,h));coverage=float((mask>.5).mean());valid+=mask_quality(coverage);frames+=1
                alpha=(np.clip((mask-.15)/.7,0,1)*255).astype(np.uint8);rgba=np.dstack([rgb,alpha]);process.stdin.write(rgba.tobytes())
    finally:
        cap.release();process.stdin.close();process.wait();log.close()
    if process.returncode:raise RuntimeError('Foreground encode failed; inspect segmentation.log')
    quality=valid/max(1,frames)
    if quality>=.85:plan.update({'mask_src':'assets/foreground.webm','mask':'validated-coverage','mask_quality_fraction':quality})
    else:plan.update({'mask':'rejected','mask_quality_fraction':quality,'fallback':'foreground captions; invalid person-mask coverage'})
    write(p/'frame-plan.json',plan);return plan
