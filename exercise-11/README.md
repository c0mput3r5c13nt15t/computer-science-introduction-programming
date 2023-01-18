# exercise-11 (19.5 / 20)

### Aufgabe 11.1: compose.py (2/2)

### Aufgabe 11.2: filter.py (4/4)
* a) (2/2)

* b) (2/2)

### Aufgabe 11.3: octs_to_int.py (2.5/3)
Ungewollter print (-0.5P)

### Aufgabe 11.4: integral.py (9/9)
* a) (2/2)

* b) (5/5)

* c) (2/2)
Sehr schön

### Aufgabe 11.5: NOTES.md (2/2)
Aussagekräftig heißt einfach nur die Funktionen für unterschiedliche Fälle zu testen.

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

## Test
```
============================= test session starts ==============================
collecting ... collected 23 items

test_11.py::test_compose_no_toplevel_code PASSED
test_11.py::test_compose_is_lambda PASSED
test_11.py::test_compose PASSED
test_11.py::test_compose_different_functions PASSED
test_11.py::test_compose_own PASSED
test_11.py::test_filter_no_toplevel_code PASSED
test_11.py::test_my_filter_is_lambda PASSED
test_11.py::test_my_diff_is_lambda PASSED
test_11.py::test_my_filter PASSED
test_11.py::test_my_filter_alphabetical PASSED
test_11.py::test_my_diff PASSED
test_11.py::test_my_diff_alphabetical PASSED
test_11.py::test_octs_to_int_no_toplevel_code PASSED
test_11.py::test_octs_to_int_is_lambda PASSED
test_11.py::test_octs_to_int PASSED
test_11.py::test_octs_to_int_own PASSED
test_11.py::test_integral_no_toplevel_code PASSED
test_11.py::test_differentiate_typing PASSED
test_11.py::test_integrate_typing PASSED
test_11.py::test_differentiate PASSED
test_11.py::test_differentiate_own PASSED
test_11.py::test_integrate PASSED
test_11.py::test_integrate_own PASSED

============================== 23 passed in 0.12s ==============================
```
