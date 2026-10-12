import unittest
from engine.speech import energy_regions, candidate_pauses, choose_voice_channel
class Analysis(unittest.TestCase):
    def test_silent_input_has_no_regions(self):
        self.assertEqual(energy_regions([0]*500,100),[])
    def test_weak_edges_and_pause_context(self):
        regions=energy_regions([0]*20+[.04]*50+[0]*180+[.04]*50+[0]*20,100)
        self.assertEqual(len(regions),2)
        candidates=candidate_pauses(regions,3200000)
        self.assertEqual(len(candidates),1)
        self.assertGreater(candidates[0]['start_us'],regions[0]['end_us'])
        self.assertLess(candidates[0]['end_us'],regions[1]['start_us'])
    def test_voice_on_right_survives(self):
        self.assertEqual(choose_voice_channel([{'speech_us':0,'rms':.1},{'speech_us':5000000,'rms':.04}]),1)
    def test_continuous_speech_is_an_island(self):
        self.assertEqual(len(energy_regions([.04]*500,100)),1)
    def test_idle_edges_leave_acoustic_padding(self):
        cs=candidate_pauses([{'start_us':1500000,'end_us':3000000}],5000000)
        self.assertEqual([c['id'] for c in cs],['idle-start','idle-end'])
        self.assertLess(cs[0]['end_us'],1500000);self.assertGreater(cs[1]['start_us'],3000000)
