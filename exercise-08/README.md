# exercise-08 (19.5 / 20)

## Feedback

### Aufgabe 8.1 - Vererbung - fleet.py (15.5/16)
- Typannotationen für `self` sind nicht nötig, das ist zuviel Schreibarbeit :-)

#### Aufgabe 8.1 a) - Klassenhierarchie (6/6)
- Top!

#### Aufgabe 8.1 b) - post_init (4/4)
- Läuft!

#### Aufgabe 8.1 c) - Methoden (5.5/6)
- `alter()` sollte ohne -1 sein, das ist aber unser Fehler.
- `maut()` bei `LKW` vergessen, was die doppelte Maut von `Kraftfahrzeug` sein
sollte. [-0.5P]

### Aufgabe 8.2 - Testing - test_fleet.py (2/2)
- Top!

### Aufgabe 8.3 - Erfahrungen - NOTES.md (2/2)
- `pytest` müsste dafür in Deine Umgebungsvariablen eingebunden werden. Der
Aufruf über `python3 -m pytest` ist aber absolut richtig. Für `pytest` müsstest
Du also den Aufruf mit `python3 -m pytest` ersetzen.
- Zum Einen stimm ich Dir dazu, dass es etwas repetitiv ist, zum Anderen muss
ich aber auch sagen, dass damit das Niveau nicht zu hoch angesetzt wird, denn
es gibt hier einige kleine Stolperfallen, die schnell Punkte kosten können. So
mag das für die einen zwar etwas langweilig sein, für die anderen aber schon
herausfordernd genug, dass die froh sind, dass es ein wenig Wiederholung gibt.
- Mehr Tests werden noch kommen :-)
- Und ja, das wäre vielleicht geschickter gewesen direkt `int` zu fordern.
- Schönes Blatt!

### Anmerkungen:
- Wenn Du Fragen zur Korrektur hast, kannst Du gerne eine Mail an mich oder in
  die NOTES.md schreiben.
- Fragen zur Vorlesung und zu den Übungen stellst Du am besten in den Chat auf
  https://chat.laurel.informatik.uni-freiburg.de damit alle etwas von der
  Antwort haben.
- Kevin <kevin.kruessenberg@merkur.uni-freiburg.de>

## Build 🟢 (success)
### initialize 🟢 (success)
```bash
git clone $GITEA_PROTOCOL://$GITEA_USER:$GITEA_PASSWORD@$GITEA_HOST/$COURSE/$STUDENT.git $STUDENT
```
### lint 🟢 (success)
```bash
pycodestyle --ignore=E501,W292,E704,W503,W504,E731 /$STUDENT/$EXERCISE
```
### compile 🟢 (success)
```bash
for py in $STUDENT/$EXERCISE/*.py; do [ -f $py ] || continue; python3.10 -m py_compile $py; done
```
### notes 🟢 (success)
```bash
./validate_notes $STUDENT $EXERCISE
```

## Tests

```
============================= test session starts ==============================
collecting ... collected 22 items

🟢 test_08.py::Fleet::test_Bus PASSED
🟢 test_08.py::Fleet::test_Fahrrad PASSED
🟢 test_08.py::Fleet::test_Fahrzeug PASSED
🟢 test_08.py::Fleet::test_Kraftfahrzeug PASSED
🟢 test_08.py::Fleet::test_LKW PASSED
🟢 test_08.py::Fleet::test_PKW PASSED
🔴 test_08.py::Fleet::test_alter FAILED
🔴 test_08.py::Fleet::test_annot FAILED
🟢 test_08.py::Fleet::test_gewicht PASSED
🔴 test_08.py::Fleet::test_marktwert FAILED
🔴 test_08.py::Fleet::test_maut FAILED
🟢 test_08.py::Fleet::test_plaetze PASSED
🟢 test_08.py::Fleet::test_post_init_baujahr PASSED
🟢 test_08.py::Fleet::test_post_init_leergewicht PASSED
🟢 test_08.py::Fleet::test_post_init_leistung PASSED
🟢 test_08.py::Fleet::test_post_init_neupreis PASSED
🟢 test_08.py::Fleet::test_post_init_rahmengroesse PASSED
🟢 test_08.py::Fleet::test_post_init_sitzplaetze PASSED
🟢 test_08.py::Fleet::test_post_init_stehplaetze PASSED
🟢 test_08.py::Fleet::test_post_init_super PASSED
🟢 test_08.py::Fleet::test_post_init_zuladung PASSED
🟢 test_08.py::Fleet::test_post_init_zustand PASSED

========================= 4 failed, 18 passed in 0.09s =========================
```
