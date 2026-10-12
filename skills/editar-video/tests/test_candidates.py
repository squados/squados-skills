import unittest
from engine.candidates import semantic_candidates
from engine.cuts import validate_decisions
class Candidates(unittest.TestCase):
    def test_editor_phrase_only_proposes_never_authorizes_cut(self):
        s=[{'text':'Editor, tira isso.','start_us':100000,'end_us':900000},{'text':'O autor disse editor na entrevista.','start_us':1200000,'end_us':2000000}]
        cs=semantic_candidates(s,2500000);self.assertEqual(len([c for c in cs if c['kind']=='editor-instruction']),1)
        a={'duration_us':2500000,'words':[{'id':'w1','text':'Editor','start_us':100000,'end_us':300000}],'candidates':cs}
        r={'candidate_id':'instruction-0','start_us':40000,'end_us':980000,'reason':'instruction','evidence':'similar text'}
        with self.assertRaises(ValueError):validate_decisions(a,{'removals':[r]})
        r['instruction_confirmed']=True;r['semantic_preserved']=True
        self.assertEqual(len(validate_decisions(a,{'removals':[r]})),1)
