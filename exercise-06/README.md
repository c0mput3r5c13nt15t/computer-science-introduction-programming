# exercise-06 (18.5 / 20)

## Feedback

### Aufgabe 6.1 - Supermarkt - supermarket.py (8/8)

#### Aufgabe 6.1 a) - Datenklassen (2/2)
- Top!

#### Aufgabe 6.1 b) - is_expired (2/2)
- Sehr geschickte Lösung! `match stock.kind` wäre der Einfachheit halber auch
möglich gewesen :-)

#### Aufgabe 6.1 c) - get_expired (2/2)
- Läuft.

#### Aufgabe 6.1 d) - buy (2/2)
- Sehr gut!

### Aufgabe 6.2 - Mailserver - mail.py (8.5/10)

#### Aufgabe 6.2 a) - Datenklassen (2/2)
- Passt.

#### Aufgabe 6.2 b) - show_mail_* (1.5/2)
- Bei `show_mail` fehlt ein Absatz nach `subject`. Bitte besser aufpassen ;-)
- Der Rest sieht gut aus.

#### Aufgabe 6.2 d) - find_server (1.5/2)
- Die Reihenfolge der Parameter muss wie auf dem Übungsblatt sein! [-0.5P]
- Das heißt: zuerst `domain`, dann erst `servers`, analog bei `find_account`.
Dadurch schlagen übrigens auch die Tests fehl.

#### Aufgabe 6.2 e) - deliver_mail (2/2)
- Passt.

#### Aufgabe 6.2 f) - deliver_all_mail (1.5/2)
- E-Mails deren Absenderadresse nicht authentisch ist werden gelöscht. Das wird
bei Dir allerdings nicht berücksichtigt., sondern nur erfolgreich zugestellte
E-Mails werden aus der `outbox` entfernt. [-0.5P]

### Aufgabe 6.3 - Erfahrungen - NOTES.md (2/2)

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
./validate_notes $STUDENT $EXERCISE validate_groups
```

## Tests

```
============================= test session starts ==============================
collecting ... collected 17 items

🟢 test_06.py::Supermarket::test_annotation PASSED
🟢 test_06.py::Supermarket::test_buy PASSED
🟢 test_06.py::Supermarket::test_classes PASSED
🟢 test_06.py::Supermarket::test_get_expired PASSED
🟢 test_06.py::Supermarket::test_is_expired PASSED
🟢 test_06.py::Supermarket::test_tests PASSED
🔴 test_06.py::Mail::test_annotation FAILED
🟢 test_06.py::Mail::test_classes PASSED
🔴 test_06.py::Mail::test_deliver_all_mail FAILED
🟢 test_06.py::Mail::test_deliver_mail PASSED
🔴 test_06.py::Mail::test_find_account FAILED
🔴 test_06.py::Mail::test_find_server FAILED
🔴 test_06.py::Mail::test_show_mail FAILED
🟢 test_06.py::Mail::test_show_mail_account PASSED
🟢 test_06.py::Mail::test_show_mail_address PASSED
🟢 test_06.py::Mail::test_show_mail_server PASSED
🟢 test_06.py::Mail::test_tests PASSED

========================= 5 failed, 12 passed in 0.06s =========================
```
