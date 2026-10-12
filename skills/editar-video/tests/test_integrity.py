import unittest,tempfile
from unittest.mock import patch
from types import SimpleNamespace
from pathlib import Path
from engine.state import write,fingerprint
from engine.export import config_fingerprint,export_project,assert_composed
from engine.revision import revise_board
from engine.cuts import apply_edit

class Integrity(unittest.TestCase):
    def test_compose_removes_residual_music_mix(self):
        from scripts.run import compose
        from engine.storyboard import default_storyboard
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'assets').mkdir();(p/'assets/mix.wav').write_bytes(b'old voice and music')
            words=[{'id':'w1','text':'fala.','start_us':0,'end_us':1000000}]
            write(p/'edit.json',{'words':words});write(p/'storyboard.json',default_storyboard(words))
            with patch('scripts.run.run'):compose(SimpleNamespace(project=p,storyboard=None,style=None))
            self.assertFalse((p/'assets/mix.wav').exists())
    def test_render_rejects_changed_inputs(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);write(p/'storyboard.json',{'value':15});(p/'index.html').write_text('compiled')
            write(p/'composition-state.json',{'fingerprint':config_fingerprint(p)})
            assert_composed(p);write(p/'storyboard.json',{'value':50})
            with self.assertRaises(ValueError):assert_composed(p)
    def test_export_rejects_replaced_master(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'master.mp4').write_bytes(b'checked')
            write(p/'qa.json',{'technical_passed':True,'fingerprint':config_fingerprint(p),'master_sha256':fingerprint([p/'master.mp4'])})
            (p/'master.mp4').write_bytes(b'replaced')
            with self.assertRaises(ValueError):export_project(p)
    def test_caption_revision_invalidates_dependent_card(self):
        words=[{'id':'w1','text':'50','start_us':0,'end_us':1000000}]
        board={'beats':[{'id':'b1','word_ids':['w1'],'effect':'counter','data':{'value':15}}],'transitions':[]}
        revised=revise_board(board,words,{'caption_text':{'w1':'50'},'music':None,'sfx':[]})
        self.assertEqual(revised['beats'][0]['data']['text'],'50');self.assertEqual(revised['beats'][0]['effect'],'emphasis');self.assertIsNone(revised['music'])
    def test_removed_correction_valid_but_unknown_id_rejected(self):
        a={'duration_us':3000000,'candidates':[],'words':[{'id':'w1','text':'fala','start_us':0,'end_us':1000000},{'id':'w2','text':'fica','start_us':2000000,'end_us':2500000}]}
        d={'caption_corrections':{'w1':'Fala'},'removals':[{'start_us':0,'end_us':1500000,'explicit_revision':True,'reason':'requested','evidence':'user'}]}
        self.assertEqual(apply_edit(a,d)['words'][0]['id'],'w2')
        d['caption_corrections']['missing']='x'
        with self.assertRaises(ValueError):apply_edit(a,d)
