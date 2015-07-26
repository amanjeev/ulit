# ulit - You Lost In Translations


Ever wondered what happens when you try to translate some text of a language, stepwise into various intermediate langauges and back into the original langauge? I know that makes little sense but here is an example.

## Example

Given the steps to be followed : `['fr', 'uk', 'it', 'ru', 'pl', 'be', 'de', 'es']` and language of interest is `'en'`.

Starting text in `'en'`: `"When you are courting a nice girl an hour seems like a second. When you sit on a red-hot cinder a second seems like an hour. That's relativity."`

`'en'` to `'fr'`: `"Lorsque vous courtiser une jolie fille une heure semble être une seconde. Lorsque vous vous asseyez sur un rouge-chaud cinder une seconde semble une heure. C'est la relativité."`

`'fr'` to `'uk'`: `"Коли ви залицяння красивою дівчиною, годину здається секундою. Коли ви сідаєте на червоний-теплий cinder другий, здається, годину. Це в теорії відносності."`

....

Finally, `'es'` to `'en'`: `"If flirting a beautiful Girl, apparently, now the second. If She is hot and red, for a second, it seems that h in the Theory of Relativity."`

See usage section for more details.


## Usage

```
import ulit

cascade_steps = ['fr', 'uk', 'it', 'ru', 'pl', 'be', 'de', 'es']
initial_language = "en"
text = "When you are courting a nice girl an hour seems like a second. When you sit on a red-hot cinder a second seems like an hour. That's relativity."
translate = ulit.Ulit("yandex", "YOUR YANDEX TRANSLATE API KEY HERE", loglevel="DEBUG")

all_translations_steps, final_translation = translate.service.translate_cascade(initial_language=initial_language,
											                                     cascade_steps=cascade_steps,
    										                                     text=text)
    										                                     

"""
\# Output: all_translations_steps
{   
     'it': 'Quando si corteggiamento di una bella ragazza, ora sembra assecondare. Quando si prende il rosso e il caldo cinder secondo, sembra ora. Questo nella teoria della relatività.',
    'ru': 'Когда он флиртует красивая девушка, теперь, кажется, второй. Когда вы берете красный и горячий cinder второй, кажется, час. Это в теории относительности.',
    'de': 'Wenn er flirtet ein schönes Mädchen, scheint es jetzt, die zweite. Wenn Sie heiß und rot eine zweite, es scheint, dass h in der Theorie der Relativität.',
    'es': 'Si coquetea una Chica hermosa, al parecer, ahora, la segunda. Si Ella es caliente y rojo, un segundo, parece que h en la Teoría de la Relatividad.',
    'pl': 'Kiedy on flirtuje piękna dziewczyna, teraz wydaje się być drugi. Jeśli wziąć czerwony i gorący cinder drugie, wydaje się, godz. To w teorii względności.',
    'en': 'If flirting a beautiful Girl, apparently, now the second. If She is hot and red, for a second, it seems that h in the Theory of Relativity.',
    'uk': 'Коли ви залицяння красивою дівчиною, годину здається секундою. Коли ви сідаєте на червоний-теплий cinder другий, здається, годину. Це в теорії відносності.',
    'fr': "Lorsque vous courtiser une jolie fille une heure semble être une seconde. Lorsque vous vous asseyez sur un rouge-chaud cinder une seconde semble une heure. C'est la relativité.",
    'be': 'Калі ен фліртуе прыгожая дзяўчына, цяпер, здаецца, другі. Калі ўзяць чырвоны і гарачы бегавая-другое, здаецца, ч То ў тэорыі адноснасці.'
}


\# Output: final_translation

If flirting a beautiful Girl, apparently, now the second. If She is hot and red, for a second, it seems that h in the Theory of Relativity.
"""	                                            

```

## TBD

* Fix Google's stuff. Google blocked me from using their translate API in the first 20 minutes of the development. Apparently, they say I violated their TOS.
* Add tests