import unittest,tempfile,json
from pathlib import Path
from scripts.package import validate_package
class Package(unittest.TestCase):
    def test_missing_resource_blocks_distribution(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder);(p/'SKILL.md').write_text('---\nname: test\ndescription: test\n---\n[missing](references/missing.md)')
            with self.assertRaises(ValueError):validate_package(p)
    def test_canonical_package_has_real_resources(self):
        root=Path(__file__).resolve().parents[1]
        result=validate_package(root);self.assertGreater(result['files'],20)
