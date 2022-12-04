# exercise-05 (20 / 20)

## Feedback

### Allgemein
- Sehr schön mit den Docstrings :-)

### Aufgabe 5.1 - Galgenmännchen - hangman.py (9/9)

#### Aufgabe 5.1 a) - input_choice (2/2)
- Top! Sehr schön mit den f-Strings!

#### Aufgabe 5.1 b) - shape (2/2)
- Jep!

#### Aufgabe 5.1 c) - hangman (4/4)
- Sehr gut. Vorallem, dass man bei einem schon geratenen Buchstaben Bescheid
bekommt!

#### Aufgabe 5.1 d) - main (1/1)
- Was soll ich sagen? Läuft!

### Aufgabe 5.2 - Mandelbrot - mandelbrot.py (9/9)

#### Aufgabe 5.2 a) - mandelbrot(4/4)
- Minimaler Fehler. Entweder ist es `range(1, m)` oder `return n + 1`.

#### Aufgabe 5.2 b) - sample (3/3)
- Top!

#### Aufgabe 5.2 d) - render_mandelbrot (2/2)
- Passt.

### Aufgabe 5.3 - Erfahrungen - NOTES.md (2/2)
- Das freut mich zu hören :-). Wenn Du noch mehr schöne Mengen sehen möchtest:
die Mandelbrotmenge ist eigentlich nur zur Klassifizierung von Julia-Mengen
gedacht gewesen und alles fällt in die Kategorie der Fraktale. Angefangen mit
sowas wie der Koch'schen-Schneeflocke, dem Sierpinski-Dreieck bis hin zu diesen
abgefahreneren Sachen wie eben der Mandelbrotmenge, Feigenbaumdiagrammen, der
Lévy-C-Kurve und und und …
- Die Umlaute dort sollten eigentlich passen. War die Dateikodierung bei Dir
auch UTF-8? Ich hab das gerade mal getestet und bei mir funktioniert das ohne
Probleme :-s

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
### notes 🟢 (success)
```bash
./validate_notes $STUDENT $EXERCISE validate_groups
```

## Tests

```
============================= test session starts ==============================
collecting ... collected 9 items

🟢 test_05.py::Hangman::test_annotation PASSED
🟢 test_05.py::Hangman::test_hangman_example PASSED
🔴 test_05.py::Hangman::test_hangman_own FAILED
🔴 test_05.py::Hangman::test_hangman_too_many_mistakes FAILED
🟢 test_05.py::Hangman::test_input_choice PASSED
🟢 test_05.py::Hangman::test_shape PASSED
🟢 test_05.py::Mandelbrot::test_annotation PASSED
🔴 test_05.py::Mandelbrot::test_mandelbrot FAILED
🟢 test_05.py::Mandelbrot::test_sample PASSED

========================= 3 failed, 6 passed in 0.04s ==========================
```
