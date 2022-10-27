# exercise-01 (18 / 20)

## Feedback

### Aufgabe 1.1 - Algorithmen - algorithms.txt (3/5)
- Präzision: du bist etwas übergenau bei deiner Interpretation von Präzision,
womit Du leider zum falschen Ergebnis kommst. [-1P]
- Das Programm terminiert nicht, was Du richtig begründet hast, und somit wird
unendlich oft b zu a addiert. Das führt dazu, dass a unendlich groß wird und
somit unendlich Speicher benötigt, womit die dynamische Finitheit auch nicht
erfüllt ist. [-1P]
- Der Rest ist absolut richtig!

### Aufgabe 1.2 - Print-Rätsel (7/7)
#### Aufgabe 1.2 a) print1.py (3/3)
- Vorsicht. Es muss `Test` und nicht `Text` heißen!
- Außerdem verwendest Du Konzepte, die so noch nicht in der Vorlesung
drangekommen sind (slicing). Das ist für dieses Blatt noch in Ordnung, in den
kommenden Blättern wird Dir dafür aber was abgezogen. Dennoch eine kreative
Lösung um möglichst exakt dem Aufgabenblatt zu entsprechen! :-)

#### Aufgabe 1.2 b) print2.py (4/4)
- Siehe oben: slicing wäre nicht nötig gewesen, aber immerhin ist die Lösung
kreativ!

### Aufgabe 1.3 - Gruppenarbeit - lovelace.txt (6/6)
- Sehr schön!

### Aufgabe 1.4 - Erfahrungen - NOTES.md (2/2)
- Was ändert sich daran, ob es eine Text- oder Markdown-Datei ist? Beides sind
Textdateien mit anderer Dateiendung. Von daher kommt es wohl eher auf den
Texteditor an, wo sich vorallem hier VS Code anbietet.
- Mach Dir nichts draus mit der Gruppe. Es wird noch weitere Gruppenaufgaben
geben und für jedes Blatt kann man auch eine andere Gruppe haben, da bist Du
also nicht festgelegt. Vielleicht findest Du ja noch ein oder zwei andere :-)
- Ada, wie Du auch geschrieben hast, gilt als erste Programmiererin und nach
ihr ist tatsächlich auch die Programmiersprache Ada benannt. Also ganz so aus
der Luft gegriffen scheint mir das nicht, wenn ich mir den Titel der Vorlesung
anschaue :-)

### Anmerkungen:
- Wenn Du Fragen zur Korrektur hast, kannst Du gerne eine Mail an mich oder in
  die NOTES.md schreiben.
- Fragen zur Vorlesung und zu den Übungen stellst Du am besten in den Chat auf
  https://chat.laurel.informatik.uni-freiburg.de damit alle etwas von der
  Antwort haben.
- Kevin <kevin.kruessenberg@merkur.uni-freiburg.de>

## Tests

```
============================= test session starts ==============================
collecting ... collected 2 items

🔴 test_01.py::PrintTest::test_print1 FAILED
🟢 test_01.py::PrintTest::test_print2 PASSED

========================= 1 failed, 1 passed in 0.02s ==========================
```
