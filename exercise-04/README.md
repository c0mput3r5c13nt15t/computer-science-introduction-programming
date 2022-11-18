# exercise-04 (20 / 20)

## Feedback

### Aufgabe 4.1 - Kurzaufgaben - list_ops.py (6/6)
- Sehr schön!

### Aufgabe 4.2 - Pi berechnen - calculate_pi.py (4/4)
- Einwandfrei!

### Aufgabe 4.3 - Primzahlen - primes.py (8/8)
- Top!
- Aber wieso `x = 2` und das `i` von `range` nicht benutzen? Hier wäre auch
einfach `for i in range(2, n + 1)` möglich gewesen ohne `x` zu brauchen.

### Aufgabe 4.4 - Erfahrungen - NOTES.md (2/2)
- Insgesamt: sehr schönes Übungsblatt vorallem mit den Docstrings! Weiter so!
- Aktuell verwenden wir relativ einfache Tests und bauen die in die Datei mit
ein. Im echten Leben bastelt man sich eine Test-Suite, die externe Tests macht.
Das heißt: man benutzt sowas wie `unittest` oder `pytest`, letzteres muss
installiert werden, und schreibt sich Tests, die in eine test_xy.py ausgelagert
werden. So machen wir das auch mit den Tests für die Übungsblätter. Innerhalb
des Tests wird dann die entsprechende Datei importiert und nicht andersrum.
Siehe auch [unittest](https://docs.python.org/3/library/unittest.html) oder
[pytest](https://docs.pytest.org/en/7.2.x/). Hier werden aber schon Konzepte
verwendet, die noch nicht in der Vorlesung drankamen.
- In der einfachsten Form schreibst Du z.B. eine `test.py` mit Inhalt:
```python
import list_ops

assert list_ops.reverse([1, 2, 3]) == [3, 2, 1], "reverse() failed!"
assert list_ops.average([1, 3]) == 2, "average() failed!"
```
Dann führst Du diese `test.py` aus.

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
./validate_notes $STUDENT $EXERCISE
```

## Tests

```
============================= test session starts ==============================
collecting ... collected 9 items

🔴 test_04.py::ListOps::test_annot FAILED
🟢 test_04.py::ListOps::test_average PASSED
🟢 test_04.py::ListOps::test_only_positive PASSED
🟢 test_04.py::ListOps::test_reverse PASSED
🔴 test_04.py::CalculatePi::test_annot FAILED
🟢 test_04.py::CalculatePi::test_calculate_pi PASSED
🟢 test_04.py::Primes::test_annot PASSED
🟢 test_04.py::Primes::test_is_prime PASSED
🟢 test_04.py::Primes::test_primes PASSED

========================= 2 failed, 7 passed in 0.04s ==========================
```
