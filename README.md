# ulit - You Lost In Translations


Ever wondered what happens when you try to translate some text of a language, stepwise into various intermediate langauges and back into the original langauge? When you start with a language and text of your choice (generally in the smae language) and translate the text into a series of languages, feeding previous result to the next one, you end up with something that generally does not look like the original text.

If that makes little sense but here is an example.


## Latest version

0.2.2

## Pypi

[https://pypi.python.org/pypi/ulit/](https://pypi.python.org/pypi/ulit/)


## Example (using Yandex's API)

Given the steps to be followed : `['fr', 'uk', 'it', 'ru', 'pl', 'be', 'de', 'es']` and language of interest is `'en'`.

Starting text in `'en'`: `"Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied. Even the interpretation and use of words involves a process of free creation."`

`'en'` to `'fr'`: `"La langue est un processus de création libre; ses lois et ses principes sont fixes, mais la manière dont les principes de génération sont utilisés est gratuit et infiniment variés. Même l'interprétation et de l'utilisation de mots implique un processus de création libre."`

`'fr'` to `'uk'`: `"Мова-це процес вільного творчості; його закони і принципи є фіксованими, але і як принципи побудови, використовуються безкоштовно, і нескінченно різноманітні. Навіть інтерпретація і використання слова передбачає процес створення безкоштовно."`

....

Finally, `'es'` to `'en'`: `"It is the Process, of free Creativity; its Laws and Principles do not change, but, as the Rules Of Construction, which is free, and is infinitely diverse. The Interpretation and Use of the Word means that the Process of Creating free of charge."`

See usage section for more details.


## Usage

Use pip to install 

```
$ pip install ulit

```

### You can either use Google or Yandex translate API with this package

```
translate = ulit.Ulit("yandex", "YOUR YANDEX TRANSLATE API KEY HERE", loglevel="DEBUG")
```
or 

```
translate = ulit.Ulit("yandex", "YOUR YANDEX TRANSLATE API KEY HERE", loglevel="DEBUG")
```

#### Using Yandex

```
import ulit

cascade_steps = ['fr', 'uk', 'it', 'ru', 'pl', 'be', 'de', 'es']
initial_language = "en"
text = "Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied. Even the interpretation and use of words involves a process of free creation."
translate = ulit.Ulit("yandex", "YOUR YANDEX TRANSLATE API KEY HERE", loglevel="DEBUG")

all_translations_steps, final_translation = translate.service.translate_cascade(initial_language=initial_language,
											                                     cascade_steps=cascade_steps,
    										                                     text=text)
    										                                     

"""
\# Output: all_translations_steps

{
    'pl': 'Mowa jest procesem wolnego kreatywności; jego prawa i zasady są niezmienne, ale, jak i zasady budowy, są za darmo, i nieskończenie zróżnicowana. Również interpretacja i wykorzystanie słowa oznacza proces tworzenia za darmo.',
    'it': "Il discorso è un processo di libera creatività; le sue leggi e i principi sono fissi, ma come principi di costruzione, sono utilizzati gratuitamente, e infinitamente vario. Anche l'interpretazione e l'uso della parola implica il processo di creazione di gratis.",
    'ru': 'Речь-это процесс свободного творчества; его законы и принципы неизменны, но, как и принципы строительства, используются бесплатно, и бесконечно разнообразен. Также интерпретация и использование слова подразумевает процесс создания бесплатно.',
    'de': 'Es ist der Prozess, der freien Kreativität; seine Gesetze und Prinzipien nicht ändern, aber, wie die Regeln der Bau -, Sie sind kostenlos, und es ist unendlich vielfältig. Auch die Interpretation und die Verwendung des Wortes bedeutet, den Prozess der Erstellung kostenlos.',
    'fr': "La langue est un processus de création libre; ses lois et ses principes sont fixes, mais la manière dont les principes de génération sont utilisés est gratuit et infiniment variés. Même l'interprétation et de l'utilisation de mots implique un processus de création libre.",
    'uk': 'Мова-це процес вільного творчості; його закони і принципи є фіксованими, але і як принципи побудови, використовуються безкоштовно, і нескінченно різноманітні. Навіть інтерпретація і використання слова передбачає процес створення безкоштовно.',
    'es': 'Es el Proceso, de la libre Creatividad; sus Leyes y Principios no cambian, pero, como las Reglas De la Construcción, que es gratuita, y es infinitamente diversa. La Interpretación y el Uso de la Palabra significa que el Proceso de Creación de forma gratuita.',
    'be': 'Гаворка-гэта працэс свабоднага творчасці; яго законы і прынцыпы нязменныя, але, як і правілы будаўніцтва, яны бясплатна, і бясконца разнастайны. Таксама інтэрпрэтацыя і выкарыстанне слова азначае працэс стварэння бясплатна.',
    'en': 'It is the Process, of free Creativity; its Laws and Principles do not change, but, as the Rules Of Construction, which is free, and is infinitely diverse. The Interpretation and Use of the Word means that the Process of Creating free of charge.'
}


\# Output: final_translation

It is the Process, of free Creativity; its Laws and Principles do not change, but, as the Rules Of Construction, which is free, and is infinitely diverse. The Interpretation and Use of the Word means that the Process of Creating free of charge.
"""	                                            

```

#### Using Google

```
import ulit

cascade_steps = ['fr', 'uk', 'it', 'ru', 'pl', 'be', 'de', 'es']
initial_language = "en"
text = "Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied. Even the interpretation and use of words involves a process of free creation."
translate = ulit.Ulit("google", "YOUR GOOGLE TRANSLATE API KEY HERE", loglevel="DEBUG")

all_translations_steps, final_translation = translate.service.translate_cascade(initial_language=initial_language,
											                                     cascade_steps=cascade_steps,
    										                                     text=text)
    										                                     

"""
\# Output: all_translations_steps

{
    'de': 'Sprache des Prozesses der freien Schöpfung; ihre Gesetze und Grundsätze festgelegt sind, aber das Prinzip der Produktionsweise frei. Auch die Interpretation und Verwendung von Wörtern findet ein Prozess der freien Schöpfung.',
    'en': 'Language of the process of free creation; its laws and principles are fixed, but the principle of free production. The interpretation and use of words involves a process of free creation.',
    'fr': 'La langue est un processus de création libre; ses lois et ses principes sont fixés, mais la manière dont les principes de la production sont utilisées est libre et infiniment varié. Même l&#39;interprétation et de l&#39;utilisation de mots implique un processus de création libre.',
    'es': 'Idioma del proceso de creación libre; sus leyes y principios son fijos, pero el principio de producción libre. La interpretación y el uso de las palabras implica un proceso de creación libre.',
    'ru': 'Язык процесс свободного создания; его законы и принципы закреплены, но принципы метода производства свободно и бесконечно разнообразны. Даже интерпретация и использование слов включает в себя процесс свободного создания.',
    'uk': 'Мова процес вільного створення; його закони і принципи закріплені, але спосіб принципи виробництва використовуються вільно і нескінченно різноманітні. Навіть інтерпретація і використання слів включає в себе процес вільного створення.',
    'it': 'Processo Lingua di libera creazione; le sue leggi e principi sono fissi, ma i principi del metodo di produzione utilizzati liberamente e infinitamente vario. Anche l&#39;interpretazione e l&#39;uso delle parole comporta un processo di creazione libera.',
    'be': 'Мова працэс свабоднага стварэння; яго законы і прынцыпы замацаваныя, але прынцып спосабу вытворчасці свабодна і плаўна. Нават інтэрпрэтацыя і выкарыстанне слоў ўключае ў сябе працэс свабоднага стварэння.',
    'pl': 'Język procesie utworzenia wolnego; jej prawa i zasady są stałe, ale zasady metody produkcji jest darmowy i płynnie. Nawet interpretacja i stosowanie słów obejmuje proces swobodnego tworzenia.'
}


\# Output: final_translation

Language of the process of free creation; its laws and principles are fixed, but the principle of free production. The interpretation and use of words involves a process of free creation.
"""	                                            

```


## Running tests

Most of it is usual but you will need to set environment variable `YANDEX_API_KEY` with your API key (and/or `GOOGLE_API_KEY` if you are using Google, as well).

```
$ export YANDEX_API_KEY=<YOUR API KEY HERE>

$ export GOOGLE_API_KEY=<YOUR API KEY HERE>

$ python setup.py test

```
