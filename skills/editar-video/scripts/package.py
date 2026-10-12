import argparse,json,re,zipfile,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.venv','node_modules','__pycache__','.models','.frame-cache','doctor.json'}
def package_files(root):
    for p in root.rglob('*'):
        if p.is_file() and not EXCLUDED.intersection(p.relative_to(root).parts) and p.suffix not in {'.log','.pyc'}:yield p
def validate_package(root):
    root=Path(root).resolve();files=list(package_files(root))
    for p in files:
        if p.is_symlink() or hasattr(p,'is_junction') and p.is_junction():raise ValueError('External link/junction in package')
        if root not in p.resolve().parents:raise ValueError('Resource escapes package')
        if p.suffix in {'.md','.json','.py','.mjs','.toml','.yaml','.ps1','.sh'}:
            text=p.read_text(encoding='utf-8-sig')
            if re.search(r'[A-Z]:[/\\]Nextcloud|[A-Z]:[/\\]Users[/\\][a-z]+|localhost:\d+|AIza[0-9A-Za-z_-]{25}|sk-proj-[A-Za-z0-9]{20}',text,re.I):raise ValueError(f'Private path/secret in {p.name}')
            if p.suffix=='.md' and 'licenses' not in p.relative_to(root).parts:
                for target in re.findall(r'\]\(([^)]+)\)',text):
                    if '://' in target or target.startswith('#'):continue
                    dest=(p.parent/target.split('#')[0]).resolve()
                    if root not in dest.parents or not dest.exists():raise ValueError(f'Missing linked resource: {target}')
    manifest=json.loads((root/'assets/manifest.json').read_text())
    for entry in manifest['fonts']+manifest.get('models',[]):
        if hashlib.sha256((root/'assets'/entry['path']).read_bytes()).hexdigest()!=entry['sha256']:raise ValueError('Asset checksum mismatch')
    if not (root/'uv.lock').exists() or not (root/'package-lock.json').exists():raise ValueError('Runtime locks missing')
    return {'files':len(files),'fonts':len(manifest['fonts']),'structural_passed':True,'release_approved':False}
def package(output):
    result=validate_package(ROOT);output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    if output.exists():raise ValueError('Output exists; choose a new package iteration')
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
        for p in package_files(ROOT):z.write(p,Path('editar-video')/p.relative_to(ROOT))
    output.with_suffix(output.suffix+'.sha256').write_text(hashlib.sha256(output.read_bytes()).hexdigest()+'  '+output.name,encoding='utf-8')
    return result
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();print(json.dumps(package(args.output) if args.output else validate_package(ROOT),indent=2))
