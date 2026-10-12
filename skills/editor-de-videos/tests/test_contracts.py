import unittest
from engine.contracts import Fps, Segment, Word, build_edit, remap_words, validate_storyboard

class Contracts(unittest.TestCase):
    def test_rational_clock(self):
        fps = Fps(30000, 1001)
        self.assertEqual(fps.frame_us(30000), 1001000000)
        self.assertEqual(fps.frame_at(1001000000), 30000)

    def test_overlapping_removals_and_single_word(self):
        edit = build_edit(3000000, [{'start_us':1000000,'end_us':1500000}, {'start_us':1200000,'end_us':1800000}])
        self.assertEqual(edit, [Segment(0,1000000,0), Segment(1800000,3000000,1000000)])
        words = remap_words([Word('w1','importante',950000,1080000,'w1')],edit)
        self.assertEqual(len(words),1)
        self.assertEqual(words[0].end_us,1000000)

    def test_invalid_ranges_fail(self):
        with self.assertRaises(ValueError): build_edit(300, [{'start_us':250,'end_us':400}])
        with self.assertRaises(ValueError): Fps(0,1)

    def test_storyboard_fidelity(self):
        words=[Word('w1','não',0,500000,'w1')]
        with self.assertRaises(ValueError): validate_storyboard(words,[],{})
        with self.assertRaises(ValueError): validate_storyboard(words,[{'id':'b1','word_ids':['w1'],'anchor_word_id':'w2'}],{})

if __name__=='__main__': unittest.main()
