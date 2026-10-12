import json
from fractions import Fraction
from .state import run

def parse_probe(data):
    video=next((s for s in data['streams'] if s.get('codec_type')=='video'),None)
    audio=[s for s in data['streams'] if s.get('codec_type')=='audio']
    if not video or not audio: raise ValueError('Input needs video and spoken audio')
    fps=Fraction(video.get('avg_frame_rate','30/1'))
    if fps<=0: fps=Fraction(30,1)
    duration=round(float(data['format']['duration'])*1e6)
    if duration<=0: raise ValueError('Empty input')
    rotation=next((s.get('rotation',0) for s in video.get('side_data_list',[]) if 'rotation' in s),0)
    w,h=video.get('width',0),video.get('height',0)
    if abs(rotation)%180==90: w,h=h,w
    return {'duration_us':duration,'width':w,'height':h,'fps':{'num':fps.numerator,'den':fps.denominator},'hdr':video.get('color_transfer') in ['smpte2084','arib-std-b67'],'rotation':rotation,'audio_streams':audio,'raw':data}
def probe(path): return parse_probe(json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',path])))
