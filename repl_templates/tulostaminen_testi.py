from io import StringIO
import sys
sys.stdout = output = StringIO()

import random
nice_words = ('hienoa', 'mahtavaa', 'jes', 'wuhuu', 'jipii', 'toimii', 'hyvä', 'whii', 'nonii', 'jeba', 'gg', 'homma hallussa', 'gj', 'hyvää työtä')

def get_nice_word():
  return random.sample(nice_words, 1)[0]

green = '\033[32m'
red = '\033[31m'

def cprint(text, color):
  reset = '\033[0m'
  print(color + text + reset)

wrong_output_er = """
Tulostuksen %s. rivillä pitäisi olla luku %s
Nyt rivillä oli %s
"""

no_output_er = """
Tähän pitäisi tulostua lukuja. Nyt ei tulostunut mitään."
"""

corrects = tuple(range(1, 1001))

correct_output = """Tulostuksen %s rivillä on oikea luku, %s!"""

def check_line(out, i):
  if out.strip() == str(corrects[i]):
    cprint(correct_output % (i + 1, get_nice_word()), green)
  else: cprint(wrong_output_er % (i + 1, i + 1, out), red)

def aja():
  sys.stdout = sys.__stdout__
  print(output.getvalue())
  if output.getvalue() == '':
    cprint(no_output_er, red)
    return
  split_out = output.getvalue().rstrip().split('\n')
  n_cor, n_res = len(corrects), len(split_out)
  for i in range(n_cor):
    if i >= n_res:
      cprint('Tulostuksesta puuttuu vielä {} riviä.'.format(n_cor - n_res), red)
      return

    check_line(split_out[i], i)
