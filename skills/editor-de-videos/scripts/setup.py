"""Project-local dependency preparation; never modifies agent profiles."""
import argparse,json,shutil,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def doctor():
    result={'python':sys.version.split()[0],'tools':{name:shutil.which(name) for name in ['node','ffmpeg','ffprobe','uv']}}
    node_major=0
    if result['tools']['node']:
        node_major=int(subprocess.check_output([result['tools']['node'],'--version'],text=True).strip().lstrip('v').split('.')[0])
    result['node_major']=node_major
    result['ready']=all(result['tools'][x] for x in ['node','ffmpeg','ffprobe']) and (3,11)<=sys.version_info[:2]<(3,13) and node_major>=22
    return result
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--install',action='store_true');args=parser.parse_args()
    info=doctor();print(json.dumps(info,indent=2))
    if not info['ready']: raise SystemExit('Agent must prepare Python 3.11-3.12, Node 22+, FFmpeg/ffprobe under host permissions before continuing')
    if args.install:
        uv=shutil.which('uv')
        if not uv: raise SystemExit('uv is required to restore the frozen Python lock; agent should install uv first')
        subprocess.run([uv,'sync','--frozen','--project',str(ROOT)],check=True)
        npm=shutil.which('npm.cmd') or shutil.which('npm')
        subprocess.run([npm,'ci','--prefix',str(ROOT)],check=True)
    (ROOT/'doctor.json').write_text(json.dumps(info,indent=2),encoding='utf-8')
if __name__=='__main__':main()
