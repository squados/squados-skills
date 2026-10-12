import unittest
from engine.audio import mix_filter
class Audio(unittest.TestCase):
    def test_ducking_keeps_voice_continuous(self):
        filt=mix_filter(True)
        self.assertIn('sidechaincompress',filt);self.assertIn('duration=first',filt);self.assertIn('asplit',filt)
