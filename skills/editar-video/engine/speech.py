"""CPU energy hysteresis; padded acoustic islands. VAD is supplied by local ASR."""
import math
import wave
from array import array

def energy_regions(energy,rate):
    if not energy or max(energy)<1e-5: return []
    levels=sorted(energy); noise=levels[int(len(levels)*.15)]; peak=levels[int(len(levels)*.9)]
    if noise>peak*.6:noise=peak*.05
    high=max(noise*2.5,peak*.18,1e-5); low=high*.55
    regions=[]; start=None; quiet=0
    for i,value in enumerate(energy+[0]*int(rate*.15)):
        if start is None and value>=high: start=i; quiet=0
        elif start is not None:
            quiet=quiet+1 if value<low else 0
            if quiet>=max(1,int(rate*.12)):
                end=i-quiet+1
                if end-start>=int(rate*.08): regions.append({'start_us':max(0,round((start/rate-.08)*1e6)), 'end_us':min(round(len(energy)/rate*1e6),round((end/rate+.12)*1e6))})
                start=None; quiet=0
    merged=[]
    for r in regions:
        if merged and r['start_us']<=merged[-1]['end_us']: merged[-1]['end_us']=max(r['end_us'],merged[-1]['end_us'])
        else: merged.append(r)
    return merged

def analyze_pcm(path):
    with wave.open(str(path),'rb') as f:
        if f.getnchannels()!=1 or f.getsampwidth()!=2: raise ValueError('Expected mono PCM16')
        samples=array('h',f.readframes(f.getnframes())); rate=f.getframerate()
    window=max(1,round(rate*.01)); energy=[]
    for a in range(0,len(samples),window):
        chunk=samples[a:a+window]; energy.append(math.sqrt(sum(x*x for x in chunk)/len(chunk))/32768)
    return {'regions':energy_regions(energy,100),'energy_rate':100,'energy':energy}

def candidate_pauses(regions,duration_us):
    result=[]
    if regions and regions[0]['start_us']>850000:result.append({'id':'idle-start','kind':'pause','start_us':0,'end_us':regions[0]['start_us']-160000,'evidence':'Measured idle lead-in with speech padding'})
    for left,right in zip(regions,regions[1:]):
        if right['start_us']-left['end_us']>850000:
            result.append({'id':f'pause-{len(result)+1}','kind':'pause','start_us':left['end_us']+120000,'end_us':right['start_us']-160000,'evidence':'Energy island gap; preserve rhetorical pause unless agent approves'})
    if regions and duration_us-regions[-1]['end_us']>850000:result.append({'id':'idle-end','kind':'pause','start_us':regions[-1]['end_us']+120000,'end_us':duration_us,'evidence':'Measured idle tail with speech padding'})
    return result

def choose_voice_channel(scores):
    if not scores:raise ValueError('No audio channels')
    return max(range(len(scores)),key=lambda i:(scores[i]['speech_us'],scores[i]['rms']))

def speech_score(path):
    from faster_whisper.vad import get_speech_timestamps
    import numpy as np
    with wave.open(str(path),'rb') as f:
        audio=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).astype(np.float32)/32768
    speech=get_speech_timestamps(audio,sampling_rate=16000)
    return {'speech_us':round(sum(s['end']-s['start'] for s in speech)/16000*1e6),'rms':float(np.sqrt(np.mean(audio*audio))) if len(audio) else 0,'vad_regions':[{'start_us':round(s['start']/16000*1e6),'end_us':round(s['end']/16000*1e6)} for s in speech]}
