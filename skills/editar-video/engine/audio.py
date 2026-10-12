from pathlib import Path
from .state import read,write,run
from .media import normalize_voice

def mix_filter(music):
    if not music:return '[0:a]anull[mix]'
    return '[0:a]asplit=2[voice][side];[1:a]volume=0.18[music];[music][side]sidechaincompress=threshold=0.025:ratio=8:attack=10:release=300[duck];[voice][duck]amix=inputs=2:duration=first:normalize=0[mix]'

def build_mix(project,music=None,sfx=None):
    p=Path(project);assets=p/'assets';args=['ffmpeg','-hide_banner','-loglevel','error','-y','-i',assets/'voice.wav']
    filters=mix_filter(bool(music));events=sfx or []
    if music:
        music=Path(music).resolve()
        if not music.is_file():raise ValueError('Provided music file missing')
        args+=['-stream_loop','-1','-i',music]
    offset=2 if music else 1
    for i,event in enumerate(events):
        src=p/event['src']
        if p.resolve() not in src.resolve().parents or not src.is_file():raise ValueError('SFX must be a provided local project asset')
        args+=['-i',src];delay=round(event['at_us']/1000)
        filters+=f';[{offset+i}:a]volume={min(.3,max(0,event.get("volume",.15)))} ,adelay={delay}:all=1[sfx{i}]'
    if events:
        filters+=';[mix]'+''.join(f'[sfx{i}]' for i in range(len(events)))+f'amix=inputs={len(events)+1}:duration=first:normalize=0[final]'
    else:filters+=';[mix]anull[final]'
    raw=assets/'mix-raw.wav';args+=['-filter_complex',filters,'-map','[final]','-ar','48000','-c:a','pcm_s24le',raw]
    run(args,p/'mix.log');levels=normalize_voice(raw,assets/'mix.wav',p/'mix-loudness.log')
    write(p/'mix.json',{'music':str(music) if music else None,'sfx':events,'loudness':levels});return assets/'mix.wav'
