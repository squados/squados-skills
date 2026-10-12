import unittest
from engine.cuts import validate_decisions
class Cuts(unittest.TestCase):
    def setUp(self):
        self.analysis={'duration_us':4000000,'candidates':[{'id':'c1','start_us':1000000,'end_us':2000000,'kind':'pause'}],'words':[{'id':'w1','text':'não','start_us':500000,'end_us':800000}]}
    def test_unsupported_semantic_removal_rejected(self):
        with self.assertRaises(ValueError): validate_decisions(self.analysis,{'removals':[{'candidate_id':'c1','start_us':0,'end_us':1500000,'reason':'retake','evidence':'word'}]})
    def test_explicit_retakes_need_restored_word_evidence(self):
        with self.assertRaises(ValueError): validate_decisions(self.analysis,{'removals':[{'start_us':500000,'end_us':800000,'reason':'retake','evidence':'similar'}]})
    def test_pause_approved_with_evidence(self):
        result=validate_decisions(self.analysis,{'removals':[{'candidate_id':'c1','start_us':1100000,'end_us':1900000,'reason':'dead air','evidence':'energy gap'}]})
        self.assertEqual(len(result),1)
    def test_replacement_cannot_be_removed_by_another_decision(self):
        analysis={'duration_us':4000000,'candidates':[{'id':'a','start_us':0,'end_us':1000000},{'id':'b','start_us':2000000,'end_us':3000000}], 'words':[{'id':'w1','text':'30','start_us':0,'end_us':500000},{'id':'w2','text':'30','start_us':2000000,'end_us':2500000}]}
        removals=[{'candidate_id':'a','start_us':0,'end_us':1000000,'reason':'retake','evidence':'words','replacement_word_ids':['w2'],'semantic_preserved':True},{'candidate_id':'b','start_us':2000000,'end_us':3000000,'reason':'retake','evidence':'words','replacement_word_ids':['w1'],'semantic_preserved':True}]
        with self.assertRaises(ValueError):validate_decisions(analysis,{'removals':removals})
