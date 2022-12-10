# Notes

Zeitbedarf: 1.3 h

## Erfahrungen
Der Befehl `pytest` hat bei mir nicht funktioniert, stattdessen konnte ich die Testsuite mit `python3 -m pytest` ausführen gibt es einen Weg das zu ändern?

Ich finde es ein wenig schade, dass wir so wenige Tests geschrieben haben. Statt die Objektstruktur soweit auszuarbeiten, hätte man einige kompliziertere Funktionen schreiben und dann auch testen können. Vor allem das implementieren von `__post_init__` war sehr repetitiv und trug meiner Meinung nach nicht viel zu einem tieferen Verständnis bei, während das Schreiben von Tests dafür sehr hilfreich gewesen wäre.

Anmerkung: Bei der Aufgabe 8.1 c) ist nicht ganz klar, ob die Rückgabe ein int sein soll, aus dem Beispiel lässt sich das zwar schließen, es sollte aber meiner Meinung nach explizit erwähnt werden.