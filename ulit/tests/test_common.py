import os
import unittest
import ulit


YANDEX_API_KEY = os.environ.get("YANDEX_API_KEY", "")

class Yandex(unittest.TestCase):

    def setUp(self):
        self.yandex_obj = ulit.Ulit('yandex', YANDEX_API_KEY)
        self.eng_text = "Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied. Even the interpretation and use of words involves a process of free creation."
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

    def test_cascade_translate_works_final(self):
        """final translations work"""
        all_translations_steps, final_translation = self.yandex_obj.service.translate_cascade(self.init_lang,
                                                                                              self.cascade_steps_working,
                                                                                              self.eng_text)
        self.assertTrue(final_translation != "" and final_translation != None)

    def test_cascade_translate_works_all(self):
        """all steps for translations work"""
        all_translations_steps, final_translation = self.yandex_obj.service.translate_cascade(self.init_lang,
                                                                                              self.cascade_steps_working,
                                                                                              self.eng_text)
        all_t = False
        for lang, translation in all_translations_steps:
            if translation != "" and translation != None:
                all_t = True
            else:
                all_t = False
                break
        self.assertTrue(all_t)
