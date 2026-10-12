from fractions import Fraction
from pathlib import Path
from xml.sax.saxutils import escape
from .state import read,write,fingerprint

def stamp(us):
    ms=round(us/1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
def srt_text(words):
    lines=[];group=[]
    def add():
        if group: lines.append(f"{len(lines)+1}\n{stamp(group[0]['start_us'])} --> {stamp(group[-1]['end_us'])}\n"+' '.join(w['text'] for w in group)+'\n')
    for word in words:
        if group and word['start_us']-group[-1]['end_us']>800000: add();group=[]
        group.append(word)
        if len(group)>=7 or word['text'].endswith(('.', '?', '!')):add();group=[]
    add();return '\n'.join(lines)
def _time(us):
    f=Fraction(us,1000000);return f'{f.numerator}s' if f.denominator==1 else f'{f.numerator}/{f.denominator}s'
def fcpxml_text(segments,source,fps,width,height,source_duration_us):
    duration=sum(s['source_end_us']-s['source_start_us'] for s in segments)
    clips=''.join(f'<asset-clip ref="r2" offset="{_time(s["output_start_us"])}" start="{_time(s["source_start_us"])}" duration="{_time(s["source_end_us"]-s["source_start_us"])}"/>' for s in segments)
    return f'<?xml version="1.0" encoding="UTF-8"?><fcpxml version="1.10"><resources><format id="r1" frameDuration="{fps["den"]}/{fps["num"]}s" width="{width}" height="{height}"/><asset id="r2" name="source" start="0s" duration="{_time(source_duration_us)}" hasVideo="1" hasAudio="1" format="r1"><media-rep kind="original-media" src="{escape(Path(source).resolve().as_uri())}"/></asset></resources><library><event name="Editor de Vídeos"><project name="Montagem"><sequence format="r1" duration="{_time(duration)}"><spine>{clips}</spine></sequence></project></event></library></fcpxml>'
def config_fingerprint(project):
    project=Path(project)
    names=['request.json','media.json','decisions.json','edit.json','storyboard.json','frame-plan.json','index.html']
    paths=[project/n for n in names if (project/n).exists()];paths+=list((project/'assets').glob('*'))
    return fingerprint([p for p in paths if p.is_file()])

def assert_composed(project):
    project=Path(project)
    if not (project/'composition-state.json').exists() or read(project/'composition-state.json')['fingerprint']!=config_fingerprint(project):
        raise ValueError('Composition changed or was not compiled; run compose before render')
def export_project(project,timeline=None):
    project=Path(project);qa=read(project/'qa.json')
    if not qa['technical_passed'] or qa['fingerprint']!=config_fingerprint(project) or qa.get('master_sha256')!=fingerprint([project/'master.mp4']): raise ValueError('QA failed or master/configuration changed; rerender/recheck before export')
    edit=read(project/'edit.json');media=read(project/'media.json');request=read(project/'request.json')
    (project/'captions.srt').write_text(srt_text(edit['words']),encoding='utf-8')
    (project/'transcript.txt').write_text(' '.join(w['text'] for w in edit['words']),encoding='utf-8')
    if timeline:
        if timeline!='fcpxml': raise ValueError('Only experimental FCPXML currently supported')
        source=project/'source'/request['source_name'];(project/'timeline.fcpxml').write_text(fcpxml_text(edit['segments'],source,media['fps'],media['width'],media['height'],media['duration_us']),encoding='utf-8')
    summary={'video':str(project/'master.mp4'),'captions':str(project/'captions.srt'),'cuts':edit['removals'],'review_status':qa['review_status'],'timeline':'experimental rough cut; no native motion/caption keyframes' if timeline else None,'diagnostics':read(project/'composition-diagnostics.json')}
    write(project/'delivery.json',summary);return summary
