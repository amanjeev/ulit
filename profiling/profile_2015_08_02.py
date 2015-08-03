import cProfile
import pstats
import ulit

# services
YANDEX_API_KEY = os.environ.get("YANDEX_API_KEY", "")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
y = ulit.Ulit("yandex", YANDEX_API_KEY)
g = ulit.Ulit("google", GOOGLE_API_KEY)

# simple english
cascade_steps = ['fr', 'uk', 'it', 'ru', 'pl', 'be', 'de', 'es']
initial_language = "en"
text = "Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied. Even the interpretation and use of words involves a process of free creation."

cProfile.run('y.service.translate_cascade(initial_language, cascade_steps, text)', 'yandex_simple_english')
cProfile.run('g.service.translate_cascade(initial_language, cascade_steps, text)', 'google_simple_english')

text="Language is my whore, my mistress, my wife, my pen-friend, my check-out girl. Language is a complimentary moist lemon-scented cleansing square or handy freshen-up wipette. Language is the breath of God, the dew on a fresh apple, it's the soft rain of dust that falls into a shaft of morning sun when you pull from an old bookshelf a forgotten volume of erotic diaries; language is the faint scent of urine on a pair of boxer shorts, it's a half-remembered childhood birthday party, a creak on the stair, a spluttering match held to a frosted pane, the warm wet, trusting touch of a leaking nappy, the hulk of a charred Panzer, the underside of a granite boulder, the first downy growth on the upper lip of a Mediterranean girl, cobwebs long since overrun by an old Wellington boot."

cProfile.run('y.service.translate_cascade(initial_language, cascade_steps, text)', 'yandex_long_text_english')
cProfile.run('g.service.translate_cascade(initial_language, cascade_steps, text)', 'google_long_text_english')


p = pstats.Stats("yandex_simple_english")
p.sort_stats('cumulative').print_stats(5)

p = pstats.Stats("google_simple_english")
p.sort_stats('cumulative').print_stats(5)

p = pstats.Stats("yandex_long_text_english")
p.sort_stats('cumulative').print_stats(5)

p = pstats.Stats("google_long_text_english")
p.sort_stats('cumulative').print_stats(5)


"""
Sun Aug  2 22:11:33 2015    yandex_simple_english
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.486   10.486 /Users/AJ/projects/ulit-project/ulit/ulit/yandex.py:17(translate_cascade)


Sun Aug  2 22:11:36 2015    google_simple_english
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.632    2.632 /Users/AJ/projects/ulit-project/ulit/ulit/google.py:24(translate_cascade)


Sun Aug  2 22:11:52 2015    yandex_long_text_english
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   15.995   15.995 /Users/AJ/projects/ulit-project/ulit/ulit/yandex.py:17(translate_cascade)


Sun Aug  2 22:16:02 2015    google_long_text_english
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  249.982  249.982 /Users/AJ/projects/ulit-project/ulit/ulit/google.py:24(translate_cascade)
"""