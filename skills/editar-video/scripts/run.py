"""Shared CLI for Codex, Claude Code and Hermes. No provider key required."""
import argparse,shutil,sys,difflib,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from engine.state import read,write,run,fingerprint
from engine.probe import probe
from engine.speech import analyze_pcm,candidate_pauses,speech_score,choose_voice_channel
from engine.transcribe import transcribe
from engine.cuts import apply_edit
from engine.media import build_aroll
from engine.audio import build_mix
from engine.vision import detect_faces,caption_zone,segment_foreground
from engine.storyboard import default_storyboard,validate_project_storyboard
from engine.qa import check_delivery
from engine.export import export_project,config_fingerprint,assert_composed
from engine.revision import revise_board
from engine.candidates import semantic_candidates

def prepare(args):
    project=Path(args.project).resolve();source=Path(args.input).resolve()
    if (project/'request.json').exists():raise ValueError('Project exists; use revise or a new project directory')
    media=probe(source);(project/'source').mkdir(parents=True);shutil.copy2(source,project/'source'/source.name)
    request={'source_name':source.name,'source_sha256':fingerprint([source]),'aspect':args.aspect,'kind':args.kind,'direction':args.direction}
    write(project/'request.json',request);write(project/'media.json',media)
    scores=[];channel_paths=[];channels=[]
    for track,stream in enumerate(media['audio_streams'][:8]):
        for channel in range(min(8,stream.get('channels',1))):
            target=project/f'analysis-track-{track}-channel-{channel}.wav';run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',source,'-map',f'0:a:{track}','-af',f'pan=mono|c0=c{channel}','-ar','16000','-c:a','pcm_s16le',target]);channel_paths.append(target);scores.append(speech_score(target));channels.append({'track':track,'channel':channel})
    selected=choose_voice_channel(scores);pcm=project/'analysis.wav';shutil.copy2(channel_paths[selected],pcm)
    media['analysis_channel']=channels[selected]['channel'];media['analysis_track']=channels[selected]['track'];media['channel_scores']=[dict(score,**channel) for score,channel in zip(scores,channels)];write(project/'media.json',media)
    speech=analyze_pcm(pcm);speech['vad_regions']=scores[selected]['vad_regions']
    if not speech['regions'] or len(speech['regions'])==1 and speech['regions'][0]['end_us']-speech['regions'][0]['start_us']>media['duration_us']*.95:
        speech['regions']=speech['vad_regions'] or speech['regions'];speech['method']='vad-fallback'
    write(project/'speech.json',speech)
    transcript=read(args.transcript) if args.transcript else transcribe(pcm,args.model,args.language,args.glossary,project/'.models')
    write(project/'transcript.raw.json',transcript);candidates=candidate_pauses(speech['regions'],media['duration_us'])
    candidates+=semantic_candidates(transcript.get('sentences',[]),media['duration_us'])
    candidates=[c for c in candidates if c['end_us']>c['start_us']]
    analysis={'duration_us':media['duration_us'],'words':transcript['words'],'candidates':candidates,'language':transcript.get('language')}
    write(project/'analysis.json',analysis);write(project/'decisions.json',{'removals':[],'caption_corrections':{}})
    return {'project':str(project),'next':'Agent reviews analysis.json and writes decisions.json; then apply','candidates':len(candidates)}
def apply(args):
    p=Path(args.project).resolve();decisions=read(args.decisions or p/'decisions.json');edit=apply_edit(read(p/'analysis.json'),decisions)
    write(p/'decisions.json',decisions);write(p/'edit.json',edit);build_aroll(p)
    faces=detect_faces(p/'assets/aroll.mp4');frame=read(p/'frame-plan.json');frame.update({'faces':faces,'caption_zone':caption_zone(faces)});write(p/'frame-plan.json',frame)
    board=default_storyboard(edit['words'],read(p/'request.json')['direction']);write(p/'storyboard.json',board)
    return {'words':len(edit['words']),'duration_us':edit['duration_us'],'next':'Agent refines storyboard.json against kept speech; then compose'}
def compose(args):
    p=Path(args.project).resolve();board=read(args.storyboard or p/'storyboard.json')
    if args.style: board['style']=read(args.style)
    validate_project_storyboard(read(p/'edit.json')['words'],board);write(p/'storyboard.json',board)
    if any(b['caption']=='embedded' for b in board['beats']):segment_foreground(p)
    if board.get('music') or board.get('sfx'):
        music=p/board['music'] if board.get('music') else None
        if music and p not in music.resolve().parents:raise ValueError('Music must be a project asset')
        build_mix(p,music,board.get('sfx',[]))
    else:(p/'assets/mix.wav').unlink(missing_ok=True)
    run(['node',ROOT/'runtime/compile.mjs',p],p/'compile.log')
    write(p/'composition-state.json',{'fingerprint':config_fingerprint(p)})
    return {'composition':str(p/'index.html')}
def render(args):
    p=Path(args.project).resolve();assert_composed(p);os.environ['EDITAR_VIDEO_RENDER_FINGERPRINT']=config_fingerprint(p)
    run(['node',ROOT/'runtime/render.mjs',p,args.quality],p/f'render-{args.quality}.log')
    if args.quality=='final':write(p/'render-state.json',{'fingerprint':config_fingerprint(p),'master_sha256':fingerprint([p/'master.mp4'])})
    return {'video':str(p/('master.mp4' if args.quality=='final' else 'preview.mp4'))}
def revise(args):
    p=Path(args.project).resolve();patch=read(args.patch);i=2
    while p.with_name(p.name+f'-v{i}').exists():i+=1
    out=p.with_name(p.name+f'-v{i}');shutil.copytree(p,out,ignore=shutil.ignore_patterns('master.mp4','preview.mp4','visual-master.mp4','visual-preview.mp4','mix.wav','.frame-cache','.render-cache.json','review','review.json','qa.json','composition-state.json','render-state.json','delivery.json','index.html','*.log'))
    allowed={'caption_text','removals','style','beats','transitions','music','sfx','aspect','face_zoom','color','denoise'}
    if not set(patch)<=allowed:raise ValueError('Unsupported revision fields')
    decisions=read(out/'decisions.json')
    if 'caption_text' in patch:decisions['caption_corrections'].update(patch['caption_text'])
    if 'removals' in patch:decisions['removals']=patch['removals']
    write(out/'decisions.json',decisions);edit=apply_edit(read(out/'analysis.json'),decisions);write(out/'edit.json',edit)
    board=default_storyboard(edit['words'],read(out/'request.json')['direction']) if 'removals' in patch else read(out/'storyboard.json')
    board=revise_board(board,edit['words'],patch)
    validate_project_storyboard(edit['words'],board);write(out/'storyboard.json',board)
    picture={k:patch[k] for k in ['aspect','face_zoom','color','denoise'] if k in patch}
    if picture:
        request=read(out/'request.json');request.update(picture);write(out/'request.json',request)
    if 'removals' in patch or picture:
        build_aroll(out);faces=detect_faces(out/'assets/aroll.mp4');frame=read(out/'frame-plan.json');frame.update({'faces':faces,'caption_zone':caption_zone(faces)});write(out/'frame-plan.json',frame)
    return {'project':str(out),'next':'compose, render, qa, export'}
def main():
    parser=argparse.ArgumentParser();sub=parser.add_subparsers(dest='command',required=True)
    for name in ['prepare','apply','compose','render','qa','export','revise']:
        s=sub.add_parser(name);s.add_argument('--project',required=True)
        if name=='prepare':
            s.add_argument('--input',required=True);s.add_argument('--aspect',choices=['source','9:16','16:9'],default='source');s.add_argument('--kind',choices=['talking-head','screencast'],default='talking-head');s.add_argument('--direction',choices=['criador','editorial','tecnologia','aula'],default='criador');s.add_argument('--model',default='base');s.add_argument('--language');s.add_argument('--glossary',default='');s.add_argument('--transcript')
        elif name=='apply':s.add_argument('--decisions')
        elif name=='compose':s.add_argument('--storyboard');s.add_argument('--style')
        elif name=='render':s.add_argument('--quality',choices=['preview','final'],default='preview')
        elif name=='export':s.add_argument('--timeline',choices=['fcpxml'])
        elif name=='revise':s.add_argument('--patch',required=True)
    args=parser.parse_args()
    if args.command=='qa': result=check_delivery(args.project)
    elif args.command=='export':result=export_project(args.project,args.timeline)
    else:result=globals()[args.command](args)
    import json;print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
