import argparse,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
from package import validate_package
def install(destination):
    validate_package(ROOT)
    destination=Path(destination).resolve()
    if destination.exists():raise ValueError('Destination exists; preserve it and choose a new directory')
    if ROOT==destination or ROOT in destination.parents:raise ValueError('Destination cannot be inside source package')
    for p in ROOT.rglob('*'):
        if p.is_symlink():raise ValueError('Public package must contain real files')
    shutil.copytree(ROOT,destination,ignore=shutil.ignore_patterns('.venv','node_modules','__pycache__','doctor.json','.models','*.log'))
    return destination
def main():
    p=argparse.ArgumentParser();p.add_argument('--host',choices=['codex','claude','hermes'],required=True);p.add_argument('--destination',required=True);a=p.parse_args();print(install(a.destination))
if __name__=='__main__':main()
