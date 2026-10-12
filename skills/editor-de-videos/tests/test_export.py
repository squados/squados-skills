import unittest,tempfile
from pathlib import Path
from engine.export import srt_text, fcpxml_text
class Export(unittest.TestCase):
    def test_caption_money_and_time(self):
        text=srt_text([{'text':'R$ 50','start_us':1500000,'end_us':2500000}]);self.assertIn('00:00:01,500 --> 00:00:02,500',text);self.assertIn('R$ 50',text)
    def test_timeline_uses_final_source_ranges(self):
        xml=fcpxml_text([{'source_start_us':2000000,'source_end_us':5000000,'output_start_us':0}],'video.mp4',{'num':30000,'den':1001},640,360,10000000)
        self.assertIn('start="2s"',xml);self.assertIn('duration="3s"',xml);self.assertIn('frameDuration="1001/30000s"',xml)
