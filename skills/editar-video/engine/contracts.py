"""One integer microsecond clock. Ranges are half-open [start,end)."""
from dataclasses import dataclass, asdict
from fractions import Fraction

@dataclass(frozen=True)
class Fps:
    num: int
    den: int
    def __post_init__(self):
        if self.num <= 0 or self.den <= 0: raise ValueError('Invalid frame rate')
    def frame_us(self, frame): return round(Fraction(frame * self.den * 1000000, self.num))
    def frame_at(self, us): return round(Fraction(us * self.num, self.den * 1000000))

@dataclass(frozen=True)
class Segment:
    source_start_us: int
    source_end_us: int
    output_start_us: int

@dataclass(frozen=True)
class Word:
    id: str
    text: str
    start_us: int
    end_us: int
    source_id: str

def build_edit(source_duration_us, removals):
    if source_duration_us <= 0: raise ValueError('Invalid duration')
    ranges=[]
    for r in sorted(removals,key=lambda x:x['start_us']):
        a,b=r['start_us'],r['end_us']
        if not isinstance(a,int) or not isinstance(b,int) or not 0 <= a < b <= source_duration_us:
            raise ValueError('Removal outside source or invalid clock')
        if ranges and a <= ranges[-1][1]: ranges[-1][1]=max(b,ranges[-1][1])
        else: ranges.append([a,b])
    segments=[]; cursor=0; output=0
    for a,b in ranges+[[source_duration_us,source_duration_us]]:
        if a>cursor:
            segments.append(Segment(cursor,a,output)); output+=a-cursor
        cursor=b
    if not segments: raise ValueError('Cannot remove entire video')
    return segments

def remap_words(words, segments):
    result=[]
    for word in words:
        overlaps=[]
        for seg in segments:
            a=max(word.start_us,seg.source_start_us); b=min(word.end_us,seg.source_end_us)
            if b>a: overlaps.append((b-a,a,b,seg))
        if not overlaps: continue
        _,a,b,seg=max(overlaps,key=lambda x:x[0])
        result.append(Word(word.id,word.text,seg.output_start_us+a-seg.source_start_us,
                           seg.output_start_us+b-seg.source_start_us,word.source_id))
    return sorted(result,key=lambda w:(w.start_us,w.end_us))

def validate_storyboard(words, beats, style):
    ids={w.id for w in words}; seen=[]; beat_ids=set()
    for beat in beats:
        bid=beat['id']; selected=beat['word_ids']
        if bid in beat_ids or not selected or not set(selected)<=ids or beat['anchor_word_id'] not in selected:
            raise ValueError('Invalid beat anchor, ids or duplicate beat')
        beat_ids.add(bid); seen.extend(selected)
        if beat.get('effect')=='chart' and not beat.get('data',{}).get('values'):
            raise ValueError('Chart needs source values')
    if len(seen)!=len(set(seen)) or set(seen)!=ids: raise ValueError('Storyboard must cover each word exactly once')
    if len(set(style.get('fonts',{}).values()))>3: raise ValueError('At most three font families')
    return {'coverage':1.0,'beats':len(beats)}

def serialize(items): return [asdict(x) for x in items]
