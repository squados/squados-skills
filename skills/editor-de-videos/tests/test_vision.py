import unittest
from engine.vision import caption_zone, mask_quality
class Vision(unittest.TestCase):
    def test_face_overlapping_bottom_moves_caption(self):
        self.assertEqual(caption_zone([{'x':.3,'y':.55,'w':.3,'h':.4}]),'top')
    def test_empty_or_full_masks_rejected(self):
        self.assertFalse(mask_quality(0));self.assertFalse(mask_quality(1));self.assertTrue(mask_quality(.4))
