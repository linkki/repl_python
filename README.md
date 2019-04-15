# Python-materiaali

 - Linkin tekstiohjelmointikerhoihin ja miksei muuallekin
 - Hyödyntää [repl.it](repl.it):tä
 - Tehtävät voi tehdä suoraan verkossa
 - Rakennettu [Python 2017-materiaalin](https://github.com/linkki/python2017) pohjalle
 ## Hyvin keskeneräinen

# Teknistä tietoa

## Development/production konfiguraatio
Localhostissa devausta varten html-sivujen basepathin voi asettaa kohdalleen komennoilla

```./basepath dev``` -> basepath=localhost:8000

tai

```./basepath dev ${port}``` -> basepath=localhost:${port}

ja takaisin produktioon: ```./basepath prod``` -> basepath='https://linkki.github.io/repl_python'

Sivut saa pyörimään localhostiin esim. komennolla ```python3 -m http.server``` projektin juurihakemistossa.

Päivittämällä repon, muutokset tulevat automaagisesti voimaan.

## Epämääräistä järjestelyä copypasten vähennystä varten
Eri sivujen yhteinen html löytyy tiedostosta template.html.

Navigointipalkin html löytyy assets/html kansion alta.

templaten päivittäminen html-tiedostoihin onnistuu päivittämällä basepathia (katso yltä)
tai suoraan ```python3 invoke_template_update.py $(cat used_htmls.txt)```

### Uuden materiaalisivun tekeminen
Template-järjestelyn vuoksi uuden materiaalisivun tekeminen tulee aloittaa kopioimalla
template.html-tiedoston sisältö uuteen html-sivutiedostoon.

Sisältö kirjoitetaan ```<!-- PAGE CONTENT-->```-kommentten väliin, että inkove_template_update.py-skripti toimii oikein.

Uudet materiaalisivut pitää lisätä used_htmls.txt-tiedostoon, jotta
set_basepath.sh-skripti toimii oikein.

Huom. skriptit toiminevat vain linuxilla.

# TODO
Lisää materiaalia
 - Enemmän tehtäviä
   - erityisesti vertailuoperaattoille ei ole tarpeeksi tehtäviä
 - funktiot ennen toistoa?
 - pygame esimerkkejä/tehtäviä?
Parempi prod/dev säätö?
