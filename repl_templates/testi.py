from io import StringIO

import sys
sys.stdout = out = StringIO()

green = '\033[32m'
red = '\033[31m'
orange = ''
def cprint(text, color):
  reset = '\033[0m'
  print(color + text + reset)

wrong_output_er = """
Tähän pitäisi tulla teksti "Hei maailma!".
Tarkista, että koodi toimii oikein, nyt tulostui:
%s"""

no_output_er = """
Tähän pitäisi tulla teksti "Hei maailma!"
Muista että tulostaminen tapahtuu kirjoittamalla: print('tekstiä')
"""

def aja():
  sys.stdout = sys.__stdout__
  if out.getvalue() == '':
    cprint(no_output_er, red)

  elif not out.getvalue() == 'Hei maailma!\n':
    cprint(wrong_output_er % out.getvalue(),
 red)
  else:
    print(out.getvalue())
    cprint('Oikein meni, hienoa!', green)
