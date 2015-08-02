"""Helpers for Google Translate API"""

__author__ = "Amanjeev Sethi"

import logging
from apiclient.discovery import build
from .base_service import BaseService


class Google(BaseService):

    def __init__(self, api_key):
        self._api_key = api_key
        self._service = build('translate', 'v2', developerKey=self._api_key)
        self._directions = self._directions()

    def _translate(self, initial_language, target, text):
        return self._service.translations().list(
            source=initial_language,
            target=target,
            q=[text]
        ).execute()

    def translate_cascade(self, initial_language, cascade_steps, text):
        """ 1. Check for the text if the service thinks it is the same language as the user has provided
            2. Check if the services thinks steps are legit and there is no step that cannot be done
            3. Translate cascadingly
            :param initial_language: two letter string of the language user needs to start with
            :param cascade_steps: user provided steps (usually excluding the initial language)
            :param text: the text user wants to translate cascadingly
            :return: a tuple of all translations and the final translation in the original language
        """
        logging.debug(initial_language + " - " + text)
        cascade_steps = self.steps_to_execute(initial_language, cascade_steps)
        results = {}
        orig_lang = initial_language
        for lang in cascade_steps[1:]:
            try:
                response = self._translate(orig_lang, lang, text)
                results[lang] = response['translations'][0]['translatedText']
                orig_lang = lang
            except:
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
        result = self._service.detections().list(
            q=[text]
        ).execute()
        return result['detections'][0][0]['language']

    def _directions(self):
        """Service's available translation directions
        :return: list of the available translation directions (from-to)
        """
        pass

    def check_language(self, initial_language, text):
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

    def is_translation_step_valid(self, from_lang, to_lang):
        """
        If one translation step valid
        :param from_lang: two letter string for lang
        :param to_lang: two letter string for lang
        :return: boolean if translation valid from_lang to to_lang
        """
        response = self._service.languages().list(target=from_lang).execute()
        valid = False
        for lang in response['languages']:
            if lang['language'] == to_lang:
                valid = True
                break
        return valid

    def check_cascade_steps(self, initial_language, cascade_steps):
        """check if steps provided by the user are allowed by the service
        :param initial_language: two letter string of the language user needs to start with
        :param cascade_steps: user provided steps (usually excluding the initial language)
        :return: boolean of whether all the translation steps are doable
        """
        cascade_steps = self.steps_to_execute(initial_language,
                                              cascade_steps)
        is_cascade_achievable = False
        for lang in cascade_steps[1:]:
            if self.is_translation_step_valid(initial_language, lang):
                is_cascade_achievable = True
                initial_language = lang
            else:
                is_cascade_achievable = False
                break
        return is_cascade_achievable
