"""Helpers for Google Translate API"""

__author__ = "Amanjeev Sethi"

import logging
from apiclient.discovery import build
from .base_service import BaseService


class Google(BaseService):

    def __init__(self, api_key):
        self._api_key = api_key
        self._service = build('translate', 'v2', developerKey=self._api_key)

    def _translate(self, initial_language="", target="", text=""):
        return self._service.translations().list(
              source=initial_language,
              target=target,
              q=[text]
            ).execute()

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

        # print(self._service.translations().list(
        #       source='en',
        #       target='fr',
        #       q=["When you are courting a nice girl an hour seems like a second. When you sit on a red-hot cinder a second seems like an hour. That's relativity."]
        #     ).execute())
        # {'translations': [{'translatedText': 'Lorsque vous allez au devant d&#39;une jolie fille une heure semble comme une seconde. Lorsque vous vous asseyez sur une cendre rouge une seconde semble comme une heure. Voilà la relativité.'}]}
        cascade_steps = self.steps_to_execute(initial_language=initial_language,
                                              cascade_steps=cascade_steps)
        results = {}
        for lang in cascade_steps[1:]:
            try:
                 results[lang] = self._translate(initial_language=initial_language,
                                                target=lang,
                                                text=text).get("translations", "")[0].get("translatedText", "")
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
        pass

    @property
    def directions(self):
        """Service's available translation directions
        :return: list of the available translation directions (from-to)
        """
        return self._service.directions

    def check_language(self, initial_language="",
                            text=""):
        """check whether the user provided text is in the same langauge as the
         initial langauge provided by the user
        :param initial_language: two letter string of the language user needs to start with
        :param text: the text user wants to translate cascadingly
        :return: boolean whether a language is correct
        """
        pass

    def check_cascade_steps(self, cascade_steps=[]):
        """check if steps provided by the user are allowed by the service
        :param initial_language: two letter string of the language user needs to start with
        :param cascade_steps: user provided steps (usually excluding the initial language)
        :return: boolean of whether all the translation steps are doable
        """
        pass