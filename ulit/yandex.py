"""Helpers for Yandex Translate API"""

__author__ = "Amanjeev Sethi"

import logging
from yandex_translate import YandexTranslate, YandexTranslateException
from .base_service import BaseService


class Yandex(BaseService):

    def __init__(self, api_key):
        self._api_key = api_key
        self._service = YandexTranslate(self._api_key)

    def translate_cascade(self, initial_language="",
                               cascade_steps=[], text=""):
        """ 1. Check for the text if the service thinks it is the same language as the user has provided
            2. Check if the services thinks steps are legit and there is no step that cannot be done
            3. Translate cascadingly
            :param initial_language: two letter string of the language user needs to start with
            :param cascade_steps: user provided steps (usually excluding the initial language)
            :param text: the text user wants to translate cascadingly
            :return: a tuple of all translations and the final translation in the original language
        """
        logging.debug(initial_language + " - " + text)

        cascade_steps = self.steps_to_execute(initial_language=initial_language,
                                              cascade_steps=cascade_steps)
        if not self.check_language(initial_language=initial_language,
                                   text=text):
            raise YandexTranslateException(501)

        if not self.check_cascade_steps(initial_language=initial_language,
                                        cascade_steps=cascade_steps):
            raise YandexTranslateException(501)
        results = {}
        for lang in cascade_steps[1:]:
            try:
                results[lang] = self._service.translate(text, lang).get('text', '')[0]
            except YandexTranslateException:
                return {}
            text = results[lang]
            logging.debug(lang + " - " + text)
        result = results[initial_language]
        return (results, result)

    def get_language(self, text=""):
        """get the language detected by the service
           :param text: the text user wants to translate cascadingly
           :return: language detected
        """
        return self._service.detect(text)

    def check_language(self, initial_language="",
                            text=""):
        """check whether the user provided text is in the same langauge as the
         initial langauge provided by the user
        :param initial_language: two letter string of the language user needs to start with
        :param text: the text user wants to translate cascadingly
        :return: boolean whether a language is correct
        """
        lang = self.get_language(text)
        if lang == initial_language:
            is_correct_language = True
        else:
            is_correct_language = False
        return is_correct_language

    @property
    def directions(self):
        """Service's available translation directions
        :return: list of the available translation directions (from-to)
        """
        return self._service.directions

    def check_cascade_steps(self, initial_language="", cascade_steps=[]):
        """check if steps provided by the user are allowed by the service
        :param initial_language: two letter string of the language user needs to start with
        :param cascade_steps: user provided steps (usually excluding the initial language)
        :return: boolean of whether all the translation steps are doable
        """
        cascade_steps = self.steps_to_execute(initial_language=initial_language,
                                              cascade_steps=cascade_steps)
        is_cascade_achievable = False
        # checking a language with itself is not allowed
        # the first item is the initial_language
        for lang in cascade_steps[1:]:
            language_pair = initial_language + "-" + lang
            logging.debug(language_pair)
            if language_pair.strip() in self.directions:
                is_cascade_achievable = True
                initial_language = lang
            else:
                is_cascade_achievable = False
                break
        return is_cascade_achievable