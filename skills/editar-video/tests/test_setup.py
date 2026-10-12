import unittest
from scripts.setup import doctor
class Setup(unittest.TestCase):
    def test_tools_exposed_without_reading_credentials(self):
        d=doctor();self.assertIn('ffprobe',d['tools']);self.assertNotIn('keys',d)
