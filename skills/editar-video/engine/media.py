import json
import re
from statistics import median
from pathlib import Path
from .state import run,read,write

def audio_filters(): return 'highpass=f=65,lowpass=f=16000'

def color_filter(settings):
    values={'brightness':0,'contrast':1,'saturation':1};values.update(settings or {})
    ranges={'brightness':(-.08,.08),'contrast':(.9,1.12),'saturation':(.85,1.15)}
    if set(values)!=set(ranges) or any(not ranges[k][0]<=v<=ranges[k][1] for k,v in values.items()):raise ValueError('Color correction must be light and bounded')
    return 'eq='+':'.join(f'{k}={v}' for k,v in values.items())

def face_crop(w,h,ow,oh,faces,kind,zoom=1):
    if kind=='screencast' or not faces:return None
    if not 1<=zoom<=1.08:raise ValueError('Face zoom limited to 1–1.08')
    # Stable crop protects every sampled face, including headroom; no guessed tracking.
    times=[f['time_us'] for f in faces]
    if len(times)!=len(set(times)):return None
    cw=min(w,h*ow/oh)/zoom;ch=cw*oh/ow
    x=max(0,min(w-cw,median((f['x']+f['w']/2)*w for f in faces)-cw/2))
    y=max(0,min(h-ch,median((f['y']+f['h']/2)*h for f in faces)-ch*.38))
    if any(f['x']*w<x+cw*.05 or (f['x']+f['w'])*w>x+cw*.95 or f['y']*h<y+ch*.03 or (f['y']+f['h'])*h>y+ch*.85 for f in faces):return None
    return f'crop={int(cw)//2*2}:{int(ch)//2*2}:{int(x)//2*2}:{int(y)//2*2},scale={ow}:{oh}'

def frame_geometry(w,h,out_w,out_h,kind='talking-head',face=None):
    # Contain is lossless default; crop only with explicit face and requested reframing.
    if face and kind!='screencast':
        return f'scale={out_w}:{out_h}:force_original_aspect_ratio=increase,crop={out_w}:{out_h}'
    return f'scale={out_w}:{out_h}:force_original_aspect_ratio=decrease,pad={out_w}:{out_h}:(ow-iw)/2:(oh-ih)/2:color=0x101217'

def normalize_voice(input_path,output,log,denoise=False):
    processing=audio_filters()+(',afftdn=nr=6:nf=-35:tn=1' if denoise else '')+',acompressor=threshold=0.125:ratio=2:attack=10:release=100:makeup=1'
    args=['ffmpeg','-hide_banner','-y','-i',input_path,'-vn','-af',processing+',loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-']
    run(args,log)
    text=Path(log).read_text(); matches=re.findall(r'\{\s*"input_i".*?\}',text,re.S)
    if not matches: raise RuntimeError('No loudness measurements')
    levels=json.loads(matches[-1])
    if levels['input_i']=='-inf': raise ValueError('Silent voice cannot be normalized')
    filt=processing+f",loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={levels['input_i']}:measured_TP={levels['input_tp']}:measured_LRA={levels['input_lra']}:measured_thresh={levels['input_thresh']}:offset={levels['target_offset']}:linear=true:print_format=json"
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',input_path,'-vn','-af',filt,'-ar','48000','-c:a','pcm_s24le',output])
    return levels

def build_aroll(project):
    project=Path(project); media=read(project/'media.json'); edit=read(project/'edit.json'); request=read(project/'request.json')
    source=project/'source'/request['source_name']; assets=project/'assets'; assets.mkdir(exist_ok=True)
    w,h=media['width'],media['height']; aspect=request.get('aspect','source')
    if aspect=='9:16': ow,oh=1080,1920
    elif aspect=='16:9': ow,oh=1920,1080
    else:
        factor=min(1,1080/min(w,h),1920/max(w,h)); ow,oh=max(2,round(w*factor/2)*2),max(2,round(h*factor/2)*2)
    fps=media['fps']; rate=f"{fps['num']}/{fps['den']}"; filters=[]; concat=[]
    for i,s in enumerate(edit['segments']):
        a,b=s['source_start_us']/1e6,s['source_end_us']/1e6
        filters += [f'[0:v:0]trim=start={a}:end={b},setpts=PTS-STARTPTS[v{i}]',f"[0:a:{media.get('analysis_track',0)}]pan=mono|c0=c{media.get('analysis_channel',0)},atrim=start={a}:end={b},asetpts=PTS-STARTPTS,afade=t=in:d=0.004,afade=t=out:st={max(0,b-a-.004)}:d=0.004[a{i}]"]
        concat.append(f'[v{i}][a{i}]')
    filters.append(''.join(concat)+f"concat=n={len(concat)}:v=1:a=1[vcat][acat]")
    from .vision import detect_faces
    faces=detect_faces(source) if (aspect!='source' or request.get('face_zoom',1)>1) and request.get('kind')!='screencast' else []
    crop=face_crop(w,h,ow,oh,faces,request.get('kind','talking-head'),request.get('face_zoom',1))
    geometry=crop or frame_geometry(w,h,ow,oh,request.get('kind','talking-head'))
    tone='zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,' if media['hdr'] else ''
    filters.append(f"[vcat]{tone}{geometry},{color_filter(request.get('color'))},fps={rate},setsar=1,format=yuv420p[vout]")
    script=project/'filtergraph.txt'; script.write_text(';'.join(filters),encoding='utf-8')
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',source,'-filter_complex_script',script,'-map','[vout]','-map','[acat]','-c:v','libx264','-crf','18','-preset','fast','-c:a','aac','-ar','48000','-movflags','+faststart',assets/'aroll.mp4'],project/'aroll.log')
    levels=normalize_voice(assets/'aroll.mp4',assets/'voice.wav',project/'loudness.log',request.get('denoise',False))
    write(project/'frame-plan.json',{'width':ow,'height':oh,'mode':'face-crop' if crop else 'contain','source_faces':faces,'geometry':geometry,'color':request.get('color',{}),'faces':[],'mask':'unavailable','fallback':'foreground captions; no unverified segmentation','loudness':levels})
    return assets/'aroll.mp4'
