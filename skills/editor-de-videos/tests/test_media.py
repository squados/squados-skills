import unittest
from engine.media import frame_geometry, audio_filters,face_crop,color_filter
from engine.probe import parse_probe
class Media(unittest.TestCase):
    def test_screencast_contains_information(self):
        self.assertIn('pad=',frame_geometry(1920,1080,1080,1920,'screencast'))
    def test_hdr_explicit(self):
        data={'streams':[{'codec_type':'video','width':640,'height':360,'avg_frame_rate':'30000/1001','color_transfer':'smpte2084'},{'codec_type':'audio','channels':2}],'format':{'duration':'15'}}
        self.assertTrue(parse_probe(data)['hdr'])
        self.assertEqual(parse_probe(data)['fps'],{'num':30000,'den':1001})
    def test_no_audio_rejected(self):
        with self.assertRaises(ValueError): parse_probe({'streams':[{'codec_type':'video'}],'format':{'duration':'3'}})
    def test_audio_moderate(self):
        self.assertIn('highpass=f=65',audio_filters())
    def test_face_crop_preserves_observed_face_and_screen(self):
        faces=[{'time_us':0,'x':.5,'y':.25,'w':.12,'h':.2}]
        crop=face_crop(1920,1080,1080,1920,faces,'talking-head')
        self.assertIn('crop=',crop)
        self.assertIsNone(face_crop(1920,1080,1080,1920,faces,'screencast'))
        self.assertIsNone(face_crop(1920,1080,1080,1920,faces+[{'time_us':0,'x':.1,'y':.2,'w':.1,'h':.2}],'talking-head'))
    def test_light_color_is_bounded(self):
        self.assertIn('brightness=0.03',color_filter({'brightness':.03,'contrast':1.04,'saturation':1.02}))
        with self.assertRaises(ValueError):color_filter({'brightness':.9})
