# exercise-09 (19 / 20)

### Aufgabe 9.1: shapes.py (9/9)
Sehr schön
* a) (3/3)

* b) (3/3)

* c) (3/3)

### Aufgabe 9.2: face.py (3/3)

### Aufgabe 9.3: vector.py (5/6)
* a) (1/1)

* b) (4/5)
List comprehensions wurden noch nicht behandelt und dürfen dementsprechend nciht verwendet werden (-1P)

### Aufgabe 9.4: NOTES.md (2/2)
Die Aurichtung der y-Achse kann man sehr schnell durch ausprobieren herausfinden. ABer seh schöne Abgabe

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
collecting ... collected 0 items / 1 error

==================================== ERRORS ====================================
_________________________ ERROR collecting test_09.py __________________________
ImportError while importing test module '/mnt/c/Users/kraut/Documents/7. Semester/Info Tutorat/2022WS-EiP/m172947g/exercise-09/test_09.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/home/johannes/.local/lib/python3.10/site-packages/_pytest/python.py:618: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/home/johannes/.local/lib/python3.10/site-packages/_pytest/pathlib.py:533: in import_path
    importlib.import_module(module_name)
/usr/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1050: in _gcd_import
    ???
<frozen importlib._bootstrap>:1027: in _find_and_load
    ???
<frozen importlib._bootstrap>:1006: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:688: in _load_unlocked
    ???
/home/johannes/.local/lib/python3.10/site-packages/_pytest/assertion/rewrite.py:168: in exec_module
    exec(co, module.__dict__)
test_09.py:4: in <module>
    from geo import Vector2D, GuiWrapper
geo.py:4: in <module>
    import tkinter as tk
E   ModuleNotFoundError: No module named 'tkinter'
=========================== short test summary info ============================
ERROR test_09.py
=============================== 1 error in 0.18s ===============================
```
