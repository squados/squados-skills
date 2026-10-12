import json,re
from pathlib import Path
from .state import read,write,run,fingerprint
from .export import config_fingerprint
from .probe import probe

def validate_timing(expected_us,actual_us,fps):
    error=abs(actual_us-expected_us);return {'passed':error<=max(50000,round(1000000/fps)), 'error_us':error}
def validate_loudness(lufs,true_peak):return abs(lufs+16)<=1 and true_peak<=-1
def review_packet(project):
    project=Path(project);edit=read(project/'edit.json');board=read(project/'storyboard.json');folder=project/'review';folder.mkdir(exist_ok=True)
    times={0,max(0,edit['duration_us']-100000)}
    for s in edit['segments'][1:]: times.update([max(0,s['output_start_us']-100000),s['output_start_us']+100000])
    for beat in board['beats']:times.add((beat['start_us']+beat['end_us'])//2)
    frames=[]
    for i,us in enumerate(sorted(times)):
        target=folder/f'frame-{i:04}.jpg';run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(us/1e6),'-i',project/'master.mp4','-frames:v','1',target]);frames.append({'path':target.name,'time_us':us})
    clips=[]
    for i,s in enumerate(edit['segments'][1:]):
        start=max(0,s['output_start_us']/1e6-.6);target=folder/f'cut-{i:04}.wav'
        run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(start),'-i',project/'master.mp4','-t','1.2','-vn',target]);clips.append({'path':target.name,'time_us':s['output_start_us']})
    write(folder/'packet.json',{'frames':frames,'clips':clips,'full_preview':'../preview.mp4'});return {'frames':frames,'clips':clips}
def check_delivery(project):
    project=Path(project);master=project/'master.mp4';media=probe(master);edit=read(project/'edit.json');fps=media['fps']['num']/media['fps']['den']
    run(['node',Path(__file__).resolve().parents[1]/'runtime/check.mjs',project],project/'browser-qa.log')
    timing=validate_timing(edit['duration_us'],media['duration_us'],fps)
    run(['ffmpeg','-hide_banner','-v','error','-i',master,'-f','null','-'],project/'decode.log')
    run(['ffmpeg','-hide_banner','-i',master,'-vn','-af','loudnorm=I=-16:TP=-1:print_format=json','-f','null','-'],project/'master-loudness.log')
    measured=json.loads(re.findall(r'\{\s*"input_i".*?\}',(project/'master-loudness.log').read_text(),re.S)[-1])
    loudness={'integrated_lufs':float(measured['input_i']),'true_peak_dbtp':float(measured['input_tp'])}
    passed=timing['passed'] and validate_loudness(loudness['integrated_lufs'],loudness['true_peak_dbtp'])
    render=read(project/'render-state.json')
    stale=render['fingerprint']!=config_fingerprint(project) or render['master_sha256']!=fingerprint([master])
    request=read(project/'request.json')
    source_changed=fingerprint([project/'source'/request['source_name']])!=request['source_sha256']
    review=read(project/'review.json') if (project/'review.json').exists() else {}
    reviewed=review.get('fingerprint')==config_fingerprint(project) and review.get('master_sha256')==fingerprint([master]) and review.get('visual')=='passed' and review.get('audio')=='passed'
    result={'technical_passed':passed and not stale and not source_changed,'fingerprint':config_fingerprint(project),'master_sha256':fingerprint([master]),'timing':timing,'loudness':loudness,'stale':stale,'source_changed':source_changed,'review_status':'reviewed' if reviewed else 'review_pending','judgment':review,'limitations':['Automated metrics do not establish semantic accuracy or subtitle sync to phonemes']}
    result['browser_qa']=read(project/'browser-qa.json')['ok']
    write(project/'qa.json',result);review_packet(project);return result
