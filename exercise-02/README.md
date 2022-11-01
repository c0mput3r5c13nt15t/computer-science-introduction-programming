# exercise-02 (19.5 / 20)

## Feedback

### Aufgabe 2.1 - Arithmetische Ausdrücke - arithmetik.txt (4/4)
- Wunderbar. Nur das mit der "Männlichkeit" würde ich anders formulieren. Wie
auch bei den anderen Operationen, wie z.B. `*` wird hier der allgemeinste
Datentyp verwendet, der notwendig ist. Das gibt es auch bei anderen Sprachen.

### Aufgabe 2.2 - Celsius nach Fahrenheit - fahrenheit.py (4/4)
- Bitte noch keine Funktionen verwenden! Die Aufgabe lässt sich ohne Funktionen
lösen. Außerdem ist ein `if __name__ == '__main__':` zwar sehr löblich, aber
auch noch nicht von Notwendigkeit. Das kommt erst später :-)
- Es funktioniert trotzdem alles und sieht auch gut strukturiert aus, von daher
passt das!

### Aufgabe 2.3 - Mantelfläche des Kegels - kegel.py (4.5/5)
- Achte bitte darauf, dass die Ausgabe exakt so wie auf dem Übungsblatt
aussieht. Hier heißt es `Matelfläche` anstelle von `Mantelfläche` [-0.5P].
- Dennoch top!

### Aufgabe 2.4 - Abrunden - abrunden.py (5/5)
- Sehr schön!

### Aufgabe 2.5 - Erfahrungen - NOTES.md (2/2)
- Du bist hier definitiv etwas positiv vorbelastet, was Python / Programmieren
angeht. Wenn Du dir bei einem Konzept unsicher bist, ob Du das verwenden
darfst, schreib gerne eine Frage in den Chat oder schreib mir eine Mail, dann
versuche ich so schnell wie möglich zu antworten.
- Ab kommendem Blatt sind auch Funktionen erlaubt, was Dir dann natürlicher
vorkommen dürfte :-)
- Generell: Versuch für spätere Übungsblätter die Anforderungen genau so
einzuhalten, wie sie gefordert sind. Zum einen kannst Du durch diese
Einschränkung Python eventuell etwas vertiefen, zum anderen schult es natürlich
deine Art zu Denken und an Probleme mit nur einer geringen Auswahl an
"Werkzeugen" klarzukommen.
- `"..." % ...` wird nicht mehr empfohlen. Benutz hierfür lieber `.format` oder
am besten direkt `f-Strings`. Letztere sind zudem auch noch schneller in der
Auswertung (nicht, dass das hier ernsthaft eine Rolle spielen würde).
- Abschließend: sehr schön strukturierter Code und eine gute Lesbarkeit.
Weiter so!

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
collecting ... collected 6 items

🔴 test_02.py::Fahrenheit::test_basic FAILED
🔴 test_02.py::Fahrenheit::test_more FAILED
🔴 test_02.py::Kegel::test_basic FAILED
🔴 test_02.py::Kegel::test_more FAILED
🔴 test_02.py::Abrunden::test_basic FAILED
🔴 test_02.py::Abrunden::test_more FAILED

============================== 6 failed in 0.03s ===============================
```
