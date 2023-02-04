# exercise-13 (19 / 20)

### Aufgabe 13.1: suppress.py (4/4)
Sehr schön

### Aufgabe 13.2: state_machine.py (7/8)

* a) (1.5/2)
Ich vermute next_state() sollte innerhalb deiner Klasse sein, da ansonsten dein self ohne Typannotation wenig Sinn ergibt (-0.5P). 
* b) (2/2)
Die Zuweisungen des nächsten Schritts passen wie auch bei a)
* c) (3.5/4)
Dein erster Output ohne Input wird bei der Ausgabe übersprungen (-0.5P)

### Aufgabe 13.3: csv_parser.py (6/6)
Alles richtig
* a) (2/2)

* b) (2/2)

* c) (2/2)
Sehr elegant

### Aufgabe 13.4: NOTES.md (2/2)
Zu 13.2: Ich bin auch nicht unbedingt ein Fan dieser Aufgabe, da sie eben sehr unterschiedlich interpretiert werden kann, aber deine Lösung sieht gut aus. Bei S_Init() sagt die Typannotation, dass der Input entweder ein String (in diesem Fall also ein Sensorinput) oder ein vorheriger State ist. Bei der Inititalisierung ist dies immer ein Sensor. 
Zu 13.3: Die Liste ist nur zur besseren Darstellung, da die Funktion sich für alle Iteratoren gleich verhält. Bei der d) ist nichts gefragt, dies ist einfach nur eine Anmerkung.

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