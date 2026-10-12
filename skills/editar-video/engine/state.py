import hashlib
import json
import subprocess
from pathlib import Path

def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def write(path,data):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    temporary.replace(path)
def run(args,log=None,cwd=None):
    result=subprocess.run([str(x) for x in args],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',errors='replace')
    if log: Path(log).write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    if result.returncode: raise RuntimeError(f'{args[0]} failed: {result.stderr[-1800:]}')
    return result.stdout
def fingerprint(paths):
    h=hashlib.sha256()
    for path in sorted(map(Path,paths)):
        h.update(path.name.encode())
        with path.open('rb') as f:
            while chunk:=f.read(1024*1024): h.update(chunk)
    return h.hexdigest()
