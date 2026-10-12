import unittest
from engine.storyboard import default_storyboard, validate_project_storyboard
class Storyboard(unittest.TestCase):
    def test_default_coverage_and_negation(self):
        words=[{'id':'w1','text':'não','start_us':0,'end_us':500000},{'id':'w2','text':'custa.','start_us':500000,'end_us':1000000}]
        result=default_storyboard(words)
        self.assertEqual(result['beats'][0]['word_ids'],['w1','w2'])
        self.assertIn('não',result['beats'][0]['data']['text'])
        validate_project_storyboard(words,result)
    def test_unknown_effect_fails(self):
        words=[{'id':'w1','text':'Olá','start_us':0,'end_us':1000000}]
        result=default_storyboard(words);result['beats'][0]['effect']='made-up'
        with self.assertRaises(ValueError): validate_project_storyboard(words,result)
