from io import StringIO

import sys
sys.stdout = out = StringIO()

import random
nice_words = ('hienoa', 'mahtavaa', 'jes', 'wuhuu', 'jipii', 'toimii', 'hyvä', 'whii', 'nonii', 'jeba')

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

calculations = ('3 + 5 / 2',
                '(3 + 5) / 2',
                '"Maijan omenat"')
corrects = (13, 16, 252.5)

correct_output = """Tulostuksen %s rivillä on oikea tulos, %s!"""

def check_line(split_out, i):
  if i < len(split_out):
    try: out_val = float(split_out[i])
    except: out_val = split_out[i]
    if out_val == corrects[i]:
      cprint(correct_output % (i + 1, get_nice_word()), green)
    else: cprint(wrong_output_er % (i + 1, calculations[i], split_out[i]), red)

def aja():
  sys.stdout = sys.__stdout__

  print(out.getvalue())
  if out.getvalue() == '':
    cprint(no_output_er, red)
  else:
    split_out = out.getvalue().strip().split('\n')
    for i, correct in enumerate(corrects):
      check_line(split_out, i)

    n_res, n_cor = len(split_out), len(corrects)
    if n_res < n_cor:
      cprint('Tulostuksesta puuttuu vielä {}:n laskun vastaukset.'.format(n_cor - n_res), red)
