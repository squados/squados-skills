import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from resource_index import build_index
class ResourceIndex(unittest.TestCase):
    def test_local_diagnostics_and_runtime_never_become_required_public_links(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'doctor.json').write_text('{}');(p/'SKILL.md').write_text('skill');(p/'.venv').mkdir();(p/'.venv/private.txt').write_text('runtime')
            index=build_index(p);self.assertNotIn('doctor.json',index);self.assertNotIn('private.txt',index);self.assertIn('SKILL.md',index)
