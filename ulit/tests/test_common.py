import os
import unittest
import ulit


YANDEX_API_KEY = os.environ.get("YANDEX_API_KEY", "")

class Yandex(unittest.TestCase):

    def setUp(self):
        self.yandex_obj = ulit.Ulit('yandex', YANDEX_API_KEY)
        self.eng_text = "When you are courting a nice girl an hour seems like a second. When you sit on a red-hot cinder a second seems like an hour. That's relativity."
        self.init_lang = "en"
        self.cascade_steps_working = ['fr', 'uk', 'it', 'ru', 'pl', 'be', 'de', 'es']
        self.cascade_steps_not_working = ['fr', 'uk', 'tr', 'it', 'ru']

    def test_check_language_english(self):
        """english - langauge check works"""
        is_lang_correct = self.yandex_obj.service.check_language("en", self.eng_text)
        self.assertTrue(is_lang_correct)

    def test_get_lanaguage(self):
        """english - language returned is correct"""
        lang = self.yandex_obj.service.get_language(self.eng_text)
        self.assertEquals("en", lang)

    def test_directions(self):
        """en-fr in the directions for translation"""
        self.assertTrue("en-fr" in self.yandex_obj.service.directions)

    def test_cascade_steps_working(self):
        """cascade steps are allowed"""
        self.assertTrue(self.yandex_obj.service.check_cascade_steps(initial_language=self.init_lang,
                                                    cascade_steps=self.cascade_steps_working))

    def test_cascade_steps_not_working(self):
        """cascade steps are not allowed"""
        self.assertFalse(self.yandex_obj.service.check_cascade_steps(initial_language=self.init_lang,
                                                    cascade_steps=self.cascade_steps_not_working))

    # def test_cascade_translate_works(self):
