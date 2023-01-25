# exercise-12 (20 / 20)

### Aufgabe 12.1: generators.py (6/6)
Sehr schön
* a) (2/2)

* b) (1/1)

* c) (1/1)

* d) (1/1)

* e) (1/1)


### Aufgabe 12.2: decorators.py (7/7)
Super

### Aufgabe 12.3: tictactoe.py (5/5)
Sehr schön
* a) (1/1)

* b) (3/3)

* c) (1/1)

### Aufgabe 12.4: NOTES:md (2/2)
Warum deine Zeit für fib_fast() so hoch ist, kann ich mir auch nicht erklären. Bei mir verhalten sich die Zeiten wie erwartet (fib > fib_fast > fib_fast_and simple)
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