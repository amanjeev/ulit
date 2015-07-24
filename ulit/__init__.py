from yandex_translate import YandexTranslate, YandexTranslateException


class Ulit(YandexTranslate):
    """
    Main Ulit class
    """

    hosts = {'google': YandexTranslate,
             'yandex': YandexTranslate,}

    def __init__(self, host=None, api_key=None):
        if not host or host == "":
            raise ValueError("Please give a host value. Possible values: " + ", ".join(lhost for lhost in self.hosts))
        elif host not in self.hosts:
            raise ValueError(("Unknown host %s. Possible values: " + ", ".join(lhost for lhost in self.hosts)) % host)
        else:
            self.host = host
            self.translate = self.hosts[self.host](api_key)