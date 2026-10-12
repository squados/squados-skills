import unittest
from engine.qa import validate_timing,validate_loudness
class QA(unittest.TestCase):
    def test_drift_fails(self):
        self.assertFalse(validate_timing(1000000,1500000,30)['passed'])
    def test_one_frame_tolerance(self):
        self.assertTrue(validate_timing(1000000,1030000,30)['passed'])
    def test_true_peak_strict(self):
        self.assertFalse(validate_loudness(-16.24,-.94));self.assertTrue(validate_loudness(-16.2,-1.2))
