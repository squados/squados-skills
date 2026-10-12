"""Localized ASR evidence; never merges words or changes edit decisions automatically."""
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from engine.state import read,write,run
from engine.transcribe import transcribe
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);parser.add_argument('--start-us',type=int,required=True);parser.add_argument('--end-us',type=int,required=True);parser.add_argument('--model',default='base');args=parser.parse_args()
    p=Path(args.project);media=read(p/'media.json');a,b=args.start_us,args.end_us
    if not 0<=a<b<=media['duration_us']:raise ValueError('Localized range outside source')
    folder=p/'localized';folder.mkdir(exist_ok=True);audio=folder/f'{a}-{b}.wav';channel=media.get('analysis_channel',0)
    source=p/'source'/read(p/'request.json')['source_name']
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(a/1e6),'-i',source,'-t',str((b-a)/1e6),'-map',f"0:a:{media.get('analysis_track',0)}",'-af',f'pan=mono|c0=c{channel}','-ar','16000','-c:a','pcm_s16le',audio])
    result=transcribe(audio,args.model,read(p/'analysis.json').get('language'),cache=p/'.models')
    for word in result['words']:word['start_us']+=a;word['end_us']+=a;word['id']=f'local-{a}-{word["id"]}'
    for sentence in result['sentences']:sentence['start_us']+=a;sentence['end_us']+=a
    result['evidence_only']=True;target=folder/f'{a}-{b}.json';write(target,result);print(target.resolve())
if __name__=='__main__':main()
