import random
nice_words = ('hienoa', 'mahtavaa', 'jes', 'wuhuu', 'jipii',
              'toimii', 'hyvä', 'whii', 'nonii', 'jeba')


def get_nice_word():
    return random.sample(nice_words, 1)[0]


green = '\033[32m'
red = '\033[31m'


def cprint(text, color):
    reset = '\033[0m'
    print(color + text + reset)


wrong_output_er = """
Tulostuksen %s. rivillä pitäisi olla laskun %s tulos.
Nyt se oli %s
"""

no_output_er = """
Tähän pitäisi tulostua laskutoimitusten tuloksia. Nyt ei tulostunut mitään."
"""

correct_dict = {'kebab riisillä': 7,
                'hummeri': 20,
                'pizza margharita': 8,
                'kaurapuuro': 3}

correct_key_output = """Sanakirjasta löytyy avain '%s', %s!"""
missing_key_output = "Sanakirjasta pitäisi löytyä avain '%s'..."
correct_val_output = "Sanakirjasta löytyy arvo %s avaimelle '%s', %s!"
wrong_val_output = "Sanakirjasta pitäisi löytyä arvo %s avaimella '%s', nyt arvo on %s..."


def aja(sanakirja):
    assert isinstance(sanakirja, dict), "TestiVirhe: Muuttuja on tyyppiä {}, pitäisi olla sanakirja {}.".format(type(sanakirja), type(correct_dict))
    for key in correct_dict:
        correct_val = correct_dict[key]
        if key in sanakirja:
            cprint(correct_key_output % (key, get_nice_word()), green)
            if sanakirja[key] == correct_val:
                cprint(correct_val_output %
                       (correct_val, key, get_nice_word()), green)
            else:
                cprint(wrong_val_output %
                       (correct_val, key, sanakirja[key]), red)
        else:
            cprint(missing_key_output % key, red)
