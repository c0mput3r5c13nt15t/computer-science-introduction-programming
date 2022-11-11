# exercise-03 (19 / 20)

## Feedback

### Aufgabe 3.1 - Mantelfläche (4/4)
#### Aufgabe 3.1 a) cone_area_lib.py (2/2)
- Sehr schön!
#### Aufgabe 3.1 b) cone_area_app.py (2/2)
- Top! f-Strings for the win!

### Aufgabe 3.2 - Temperatur-Konvertierung - temperature.py (5/6)
- Bitte bitte bitte sei vorsichtig, wie Funktionen benannt sein müssen. Mach
im Zweifel copy & paste. Du hast überall(!) `celcius` anstelle von `celsius`
geschrieben. Alles andere ist tiptop und absolut richtig, aber der eine Typo
wäre im kommenden Blatt echt teuer. Pass also drauf auf :-) [-1P]

### Aufgabe 3.3 - Gruppenarbeit: Text-Adventure - game.py (8/8)
- Okay, holy moly! Da hast Du ordentlich Aufwand reingesteckt und ich kam noch
nicht dazu, dass mal ordentlich durchzuspielen. Respekt!
- Ich hab Dich mal in die Liste für die Hall of Fame eingetragen, das hast Du
Dir verdient!
- Ich benutz übrigens eh nur Ubuntu und hab daher keine Windows-Probleme mit
"play" oder so :-)
- Solche Sachen kannst Du aber noch abfragen und so im Zweifel selber
deaktivieren, indem Du try- / except-Blöcke benutzt.

### Aufgabe 3.4 - Erfahrungen - NOTES.md (2/2)
- Das freut mich sehr, dass Dir das mit dem Textadventure so gefallen hat!
- Das mit dem Leerzeichen ist natürlich ein lästiger Typo, aber gut gesehen!
Danke dafür.

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

🟢 test_03.py::ConeArea::test_app PASSED
🟢 test_03.py::ConeArea::test_lib PASSED
🟢 test_03.py::Temperature::test_app PASSED
🔴 test_03.py::Temperature::test_celsius_to_fahrenheit FAILED
🔴 test_03.py::Temperature::test_celsius_to_kelvin FAILED
🔴 test_03.py::Temperature::test_fahrenheit_to_celsius FAILED
🟢 test_03.py::Temperature::test_fahrenheit_to_kelvin PASSED
🔴 test_03.py::Temperature::test_kelvin_to_celsius FAILED
🟢 test_03.py::Temperature::test_kelvin_to_fahrenheit PASSED

========================= 4 failed, 5 passed in 0.19s ==========================
```
