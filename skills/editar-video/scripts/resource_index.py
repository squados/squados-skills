"""Build the Hermes resource listing from exactly the public-package allowlist."""
from pathlib import Path
from package import package_files
ROOT=Path(__file__).resolve().parents[1]

def build_index(root=ROOT):
    root=Path(root);entries=sorted(p for p in package_files(root) if p.name!='recursos.md')
    return '# Recursos do pacote\n\nO ZIP inteiro é necessário. Preserve todos os recursos abaixo.\n\n'+'\n'.join(f'- [{p.relative_to(root).as_posix()}](../{p.relative_to(root).as_posix()})' for p in entries)+'\n'

if __name__=='__main__':(ROOT/'references/recursos.md').write_text(build_index(),encoding='utf-8')
