"""Simple tool to translate a piece of text cascadingly,
in various languges."""

__author__ = "Amanjeev Sethi"

import logging
from .yandex import Yandex
from .google import Google


class Ulit(object):
    """
    Main Ulit class
    """

    _hosts = ['yandex', 'google']

    def __init__(self, host=None, api_key=None, loglevel="WARN"):
        if not host or host == "":
            raise ValueError("Please give a host value. Possible values: "
                             + ", ".join(lhost for lhost in self._hosts))
        elif host not in self._hosts:
            raise ValueError(("Unknown host %s. Possible values: "
                              + ", ".join(lhost for lhost in self._hosts)) % host)
        else:
            logging.basicConfig(level=loglevel.upper())
            self._host = host
            self._api_key = api_key
            self.service = self._create_translation_service()

    def _create_translation_service(self):
        if self._host == 'google':
            service = Google(self._api_key)
        elif self._host == 'yandex':
            service = Yandex(self._api_key)
        else:
            raise ValueError(("Unknown host %s. Possible values: " +
                              ", ".join(lhost for lhost in self._hosts)) % self._host)
        return service
