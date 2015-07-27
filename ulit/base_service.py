"""Base class for service helpers"""

__author__ = "Amanjeev Sethi"

import logging


class BaseService(object):

    @staticmethod
    def steps_to_execute(initial_language="", cascade_steps=[]):
        """construct the final steps to execute, checks whether the original language
        is the first and the last item in the cascade_steps
        :param initial_language: two letter string of the language user needs to start with
        :param cascade_steps: user provided steps (usually excluding the initial language)
        :return: list of language steps with first and last being the initial language
        """
        logging.debug(cascade_steps)
        steps = cascade_steps

        if steps[-1] != initial_language:
            steps.append(initial_language)

        if steps[0] != initial_language:
            steps.insert(0, initial_language)

        if cascade_steps[0] == initial_language and cascade_steps[-1] == initial_language:
            logging.info("Cascade steps already had the language of interest in the first and last positions.")
        logging.debug(steps)
        return steps
