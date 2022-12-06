# exercise-07 (20 / 20)

## Feedback

### Aufgabe 7.1 - Symbolische Arithmetik - optimizer.py (18/18)

#### Aufgabe 7.1 a) - node_to_str (2/2)
- Top!

#### Aufgabe 7.1 b) - node_to_str_if (2/2)
- Top!

#### Aufgabe 7.1 c) - optimize_step (8/8)
- Zeilen 29 - 32 brauchst Du nicht, da Du am Ende mit `case _` eh alles
abhandelst.
- Trotzdem: Schön geschrieben!

#### Aufgabe 7.1 d) - optimize_step_if (2/2)
- Läuft.

#### Aufgabe 7.1 e) - optimize (2/2)
- Hier sollte tatsächlich `Node`, nicht `Optional[Node]` übergeben werden.
- Cool gelöst! Könnte bei großen (sehr großen!) Ausdrücken aber tatsächlich zu
einem Fehler führen wenn das Rekursionslimit ("max recursion depth") erreicht
wird, also so ab einer Tiefe von 1000 bei Python.

#### Aufgabe 7.1 f) - REPL (2/2)
- Jep!

### Aufgabe 7.3 - Erfahrungen - NOTES.md (2/2)
- Sehr schönes Blatt, weiter so!
- Da hast Du absolut recht. Blöd gelaufen, aber Du siehst, auch uns passieren
mal Fehler (die so nicht sein dürfen!). Hab das direkt mal weitergegeben.
- Den Advent of Code hab ich teils schon weiterempfohlen :-). Türchen 6 hab ich
heute sogar zügig lösen können und 2015 bin ich nebenher  noch am Abarbeitem ;-)
Mit dem Empfehlen bin ich aber etwas vorsichtig. Wir hatten I/O nicht und ein
großer Teil der Aufgaben benötigt aber genau das. Später kommen Konzepte dran,
die noch unbekannt sind, vorallem werden auch Algorithmen (beliebt ist hier
Dijkstra) gefordert und da kann man sehr schnell überfordert sein, vorallem
weil man einfach ein paar Dinge wissen muss. Sowas wie: `dict`s sind schnell,
Listen zur Laufzeit zu erzeugen absolut nicht. Sprich: Algorithmen und
Datenstrukturen sollte man bestenfalls schon gehört haben. Jemand der noch
nicht ganz fit ist neigt dann auch schneller dazu frustriert zu sein oder
"schwierigen" Code zu schreiben (irgendwas zusammenstückeln, sodass es mit Ach
und Krach funktioniert).
- Prinzipiell geb ich dir aber recht: das ist ne coole Sache, vorallem auch,
wenn man mal neue Sprachen ausprobieren möchte.

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
collecting ... collected 7 items

🔴 test_07.py::Optimizer::test_annotation FAILED
🟢 test_07.py::Optimizer::test_node_to_str PASSED
🟢 test_07.py::Optimizer::test_node_to_str_if PASSED
🟢 test_07.py::Optimizer::test_optimize PASSED
🟢 test_07.py::Optimizer::test_optimize_step PASSED
🟢 test_07.py::Optimizer::test_optimize_step_if PASSED
🟢 test_07.py::Optimizer::test_repl PASSED

========================= 1 failed, 6 passed in 0.16s ==========================
```
