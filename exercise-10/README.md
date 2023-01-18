# exercise-10 (19.5 / 20)
### Aufgabe 10.1: exam.py (9.5/10)
* a) (3/3)
* b) (3.5/4)
Grenzfälle von Noten werden nicht richtig berechnet (würde je ein >= benötigen)(-0.5P)
* c) (3/3)

### Aufgabe 10.2: sierpinsky.py (5/5)
Sehr ausführlich gelöst

### Aufgabe 10.3: polynom.py (3/3)
Sehr schön

### Aufgabe 10.4: NOTES.md (2/2)
Die Unannehmlichkeiten sind natuürlich unnötig. Aber hat ja alles gut funktioniert.

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
collecting ... collected 36 items

test_10.py::test_exam_no_toplevel_code PASSED
test_10.py::test_update_points_typing PASSED
test_10.py::test_update_points PASSED
test_10.py::test_update_points_accept_change_0 PASSED
test_10.py::test_update_points_accept_negative_changes PASSED
test_10.py::test_update_points_accept_at_120 PASSED
test_10.py::test_update_points_reject_above_120 PASSED
test_10.py::test_update_points_accept_at_0 PASSED
test_10.py::test_update_points_reject_below_0 PASSED
test_10.py::test_update_points_reject_unknown_name PASSED
test_10.py::test_compute_grade_typing PASSED
test_10.py::test_compute_grade PASSED
test_10.py::test_compute_grade_not_passed PASSED
test_10.py::test_compute_grade_buckets FAILED
test_10.py::test_compute_grade_buckets_new_pass_points FAILED
test_10.py::test_cluster_by_grade_typing PASSED
test_10.py::test_cluster_by_grade PASSED
test_10.py::test_cluster_by_grade_all_grades PASSED
test_10.py::test_cluster_by_grade_1 FAILED
test_10.py::test_cluster_by_grade_2 FAILED
test_10.py::test_cluster_by_grade_3 FAILED
test_10.py::test_cluster_by_grade_4 FAILED
test_10.py::test_cluster_by_grade_honors_fail_rate FAILED
test_10.py::test_cluster_by_grade_uses_max_points FAILED
test_10.py::test_sierpinski_no_toplevel_code FAILED
test_10.py::test_sierpinski_typing FAILED
test_10.py::test_polynom_no_toplevel_code PASSED
test_10.py::test_polynom_crack_1_example_1 PASSED
test_10.py::test_polynom_crack_1_example_2 PASSED
test_10.py::test_polynom_crack_1_example_new PASSED
test_10.py::test_polynom_crack_2_example_1 PASSED
test_10.py::test_polynom_crack_2_example_2 PASSED
test_10.py::test_polynom_crack_2_example_3 PASSED
test_10.py::test_polynom_crack_2_example_new PASSED
test_10.py::test_polynom_crack_3_example_1 PASSED
test_10.py::test_polynom_crack_3_example_new PASSED

=================================== FAILURES ===================================
__________________________ test_compute_grade_buckets __________________________

    def test_compute_grade_buckets():
        student_points = {"a_student1": 120, "a_student2": 105, "b_student1": 104, "b_student2": 90, "c_student1": 75, "c_student2": 89, "d_student1": 60, "d_student2": 74}
>       assert compute_grade(student_points, 120, "a_student1") == 1 and compute_grade(student_points, 120, "a_student2") == 1
E       AssertionError: assert (1 == 1 and 2 == 1)
E        +  where 1 = compute_grade({'a_student1': 120, 'a_student2': 105, 'b_student1': 104, 'b_student2': 90, ...}, 120, 'a_student1')
E        +  and   2 = compute_grade({'a_student1': 120, 'a_student2': 105, 'b_student1': 104, 'b_student2': 90, ...}, 120, 'a_student2')

test_10.py:112: AssertionError
__________________ test_compute_grade_buckets_new_pass_points __________________

    def test_compute_grade_buckets_new_pass_points():
        student_points = {"a_student1": 120, "a_student2": 105, "b_student1": 104, "b_student2": 90, "c_student1": 75, "c_student2": 89, "d_student1": 60, "d_student2": 74}
        # to reach 40% wih max points = 200 -> new pass points = 89
        assert compute_grade(student_points, 200, "a_student1") == 3 and compute_grade(student_points, 200, "a_student2") == 4
        assert compute_grade(student_points, 200, "b_student1") == 4 and compute_grade(student_points, 200, "b_student2") == 4
>       assert compute_grade(student_points, 200, "c_student1") == 5 and compute_grade(student_points, 200, "c_student2") == 4
E       AssertionError: assert (5 == 5 and 5 == 4)
E        +  where 5 = compute_grade({'a_student1': 120, 'a_student2': 105, 'b_student1': 104, 'b_student2': 90, ...}, 200, 'c_student1')
E        +  and   5 = compute_grade({'a_student1': 120, 'a_student2': 105, 'b_student1': 104, 'b_student2': 90, ...}, 200, 'c_student2')

test_10.py:123: AssertionError
___________________________ test_cluster_by_grade_1 ____________________________

    def test_cluster_by_grade_1():
        student_points = {
            "Student 1": 120,
            "Student 2": 112,
            "Student 3": 105
        }
>       assert cluster_by_grade(student_points, 120) == {1: ["Student 1", "Student 2", "Student 3"]}
E       AssertionError: assert {1: ['Student 1', 'Student 2'], 2: ['Student 3']} == {1: ['Student 1', 'Student 2', 'Student 3']}
E         Differing items:
E         {1: ['Student 1', 'Student 2']} != {1: ['Student 1', 'Student 2', 'Student 3']}
E         Left contains 1 more item:
E         {2: ['Student 3']}
E         Full diff:
E         - {1: ['Student 1', 'Student 2', 'Student 3']}
E         + {1: ['Student 1', 'Student 2'], 2: ['Student 3']}
E         ?                              +  ++++

test_10.py:166: AssertionError
___________________________ test_cluster_by_grade_2 ____________________________

    def test_cluster_by_grade_2():
        student_points = {
            "Student 1": 104,
            "Student 2": 97,
            "Student 3": 90
        }
>       assert cluster_by_grade(student_points, 120) == {2: ["Student 1", "Student 2", "Student 3"]}
E       AssertionError: assert {2: ['Student 1', 'Student 2'], 3: ['Student 3']} == {2: ['Student 1', 'Student 2', 'Student 3']}
E         Differing items:
E         {2: ['Student 1', 'Student 2']} != {2: ['Student 1', 'Student 2', 'Student 3']}
E         Left contains 1 more item:
E         {3: ['Student 3']}
E         Full diff:
E         - {2: ['Student 1', 'Student 2', 'Student 3']}
E         + {2: ['Student 1', 'Student 2'], 3: ['Student 3']}
E         ?                              +  ++++

test_10.py:175: AssertionError
___________________________ test_cluster_by_grade_3 ____________________________

    def test_cluster_by_grade_3():
        student_points = {
            "Student 1": 89,
            "Student 2": 82,
            "Student 3": 75
        }
>       assert cluster_by_grade(student_points, 120) == {3: ["Student 1", "Student 2", "Student 3"]}
E       AssertionError: assert {3: ['Student 1', 'Student 2'], 4: ['Student 3']} == {3: ['Student 1', 'Student 2', 'Student 3']}
E         Differing items:
E         {3: ['Student 1', 'Student 2']} != {3: ['Student 1', 'Student 2', 'Student 3']}
E         Left contains 1 more item:
E         {4: ['Student 3']}
E         Full diff:
E         - {3: ['Student 1', 'Student 2', 'Student 3']}
E         + {3: ['Student 1', 'Student 2'], 4: ['Student 3']}
E         ?                              +  ++++

test_10.py:184: AssertionError
___________________________ test_cluster_by_grade_4 ____________________________

    def test_cluster_by_grade_4():
        student_points = {
            "Student 1": 74,
            "Student 2": 67,
            "Student 3": 60
        }
>       assert cluster_by_grade(student_points, 120) == {4: ["Student 1", "Student 2", "Student 3"]}
E       AssertionError: assert {4: ['Student 1', 'Student 2'], 5: ['Student 3']} == {4: ['Student 1', 'Student 2', 'Student 3']}
E         Differing items:
E         {4: ['Student 1', 'Student 2']} != {4: ['Student 1', 'Student 2', 'Student 3']}
E         Left contains 1 more item:
E         {5: ['Student 3']}
E         Full diff:
E         - {4: ['Student 1', 'Student 2', 'Student 3']}
E         + {4: ['Student 1', 'Student 2'], 5: ['Student 3']}
E         ?                              +  ++++

test_10.py:193: AssertionError
____________________ test_cluster_by_grade_honors_fail_rate ____________________

    def test_cluster_by_grade_honors_fail_rate():
        student_points = {
            "Student 1": 4,
            "Student 2": 3,
            "Student 3": 2,
            "Student 4": 1,
            "Student 5": 0,
        }
>       assert cluster_by_grade(student_points, 120) == {
            4: ["Student 1", "Student 2", "Student 3"],
            5: ["Student 4", "Student 5"],
        }
E       AssertionError: assert {4: ['Student 1', 'Student 2'], 5: ['Student 3', 'Student 4', 'Student 5']} == {4: ['Student 1', 'Student 2', 'Student 3'], 5: ['Student 4', 'Student 5']}
E         Differing items:
E         {4: ['Student 1', 'Student 2']} != {4: ['Student 1', 'Student 2', 'Student 3']}
E         {5: ['Student 3', 'Student 4', 'Student 5']} != {5: ['Student 4', 'Student 5']}
E         Full diff:
E         - {4: ['Student 1', 'Student 2', 'Student 3'], 5: ['Student 4', 'Student 5']}
E         ?                             -------------                 ^
E         + {4: ['Student 1', 'Student 2'], 5: ['Student 3', 'Student 4', 'Student 5']}
E         ?                                              ^            +++++++++++++

test_10.py:204: AssertionError
____________________ test_cluster_by_grade_uses_max_points _____________________

    def test_cluster_by_grade_uses_max_points():
        for max_points in range(20, 520, 5):
            pass_points = max_points // 2
            rest_points = max_points - pass_points
            student_points = {
                "Student 1": max_points,
                "Student 2": max_points - floor(rest_points * 0.25),
                "Student 3": max_points - ceil(rest_points * 0.25) - 1,
                "Student 4": max_points - floor(rest_points * 0.5),
                "Student 5": max_points - ceil(rest_points * 0.5) - 1,
                "Student 6": max_points - floor(rest_points * 0.75),
                "Student 7": max_points - ceil(rest_points * 0.75) - 1,
                "Student 8": pass_points,
                "Student 9": pass_points - 1,
            }
>           assert cluster_by_grade(student_points, max_points) == {
                1: ["Student 1", "Student 2"],
                2: ["Student 3", "Student 4"],
                3: ["Student 5", "Student 6"],
                4: ["Student 7", "Student 8"],
                5: ["Student 9"],
            }
E           AssertionError: assert {1: ['Student 1', 'Student 2'], 2: ['Student 3'], 3: ['Student 4', 'Student 5', 'Student 6'], 4: ['Student 7'], 5: ['Student 8', 'Student 9']} == {1: ['Student 1', 'Student 2'], 2: ['Student 3', 'Student 4'], 3: ['Student 5', 'Student 6'], 4: ['Student 7', 'Student 8'], 5: ['Student 9']}
E             Common items:
E             {1: ['Student 1', 'Student 2']}
E             Differing items:
E             {2: ['Student 3']} != {2: ['Student 3', 'Student 4']}
E             {3: ['Student 4', 'Student 5', 'Student 6']} != {3: ['Student 5', 'Student 6']}
E             {4: ['Student 7']} != {4: ['Student 7', 'Student 8']}
E             {5: ['Student 8', 'Student 9']} != {5: ['Student 9']}
E             Full diff:
E               {
E                1: ['Student 1', 'Student 2'],
E             +  2: ['Student 3'],
E             +  3: ['Student 4', 'Student 5', 'Student 6'],
E             +  4: ['Student 7'],
E             -  2: ['Student 3', 'Student 4'],
E             ?  ^            ^            ^
E             +  5: ['Student 8', 'Student 9'],
E             ?  ^            ^            ^
E             -  3: ['Student 5', 'Student 6'],
E             -  4: ['Student 7', 'Student 8'],
E             -  5: ['Student 9'],
E               }

test_10.py:225: AssertionError
_______________________ test_sierpinski_no_toplevel_code _______________________

    def test_sierpinski_no_toplevel_code():
>       check_no_toplevel_statements("sierpinski.py")

test_10.py:240: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = 'sierpinski.py'

    def check_no_toplevel_statements(filename: str):
        filepath = __get_relative_path(filename)
>       with open(filepath, "r") as f:
E       FileNotFoundError: [Errno 2] No such file or directory: '/mnt/c/Users/kraut/Documents/7. Semester/Info Tutorat/2022WS-EiP/m172947g/exercise-10/sierpinski.py'

tests_lib.py:290: FileNotFoundError
____________________________ test_sierpinski_typing ____________________________

    def test_sierpinski_typing():
>       check_typing(
            sierpinski,
            named={"size": int, "n": int}
        )

test_10.py:244: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

function = <function sierpinski at 0x7f71767a3520>, return_annotation = None
positional = [], named = {'n': <class 'int'>, 'size': <class 'int'>}

    def check_typing(function: Callable,
                     return_annotation=None,
                     positional: list[Any] = [],
                     named: dict[str, Any] = {}):
        given = function.__annotations__
        if return_annotation:
            assert given['return'] == return_annotation, 'wrong return type'
            del given['return']
        else:
            if given.get('return', None) is None:
                given.pop('return', None)
            assert 'return' not in given.keys(), 'wrong return type'
        for param, annotation in named.items():
            expected = given.get(param, None)
>           assert annotation == expected or str(annotation) == str(expected), f'wrong {param} type, {expected} expected, but got {annotation}'
E           AssertionError: wrong size type, None expected, but got <class 'int'>

tests_lib.py:239: AssertionError
=========================== short test summary info ============================
FAILED test_10.py::test_compute_grade_buckets - AssertionError: assert (1 == ...
FAILED test_10.py::test_compute_grade_buckets_new_pass_points - AssertionErro...
FAILED test_10.py::test_cluster_by_grade_1 - AssertionError: assert {1: ['Stu...
FAILED test_10.py::test_cluster_by_grade_2 - AssertionError: assert {2: ['Stu...
FAILED test_10.py::test_cluster_by_grade_3 - AssertionError: assert {3: ['Stu...
FAILED test_10.py::test_cluster_by_grade_4 - AssertionError: assert {4: ['Stu...
FAILED test_10.py::test_cluster_by_grade_honors_fail_rate - AssertionError: a...
FAILED test_10.py::test_cluster_by_grade_uses_max_points - AssertionError: as...
FAILED test_10.py::test_sierpinski_no_toplevel_code - FileNotFoundError: [Err...
FAILED test_10.py::test_sierpinski_typing - AssertionError: wrong size type, ...
======================== 10 failed, 26 passed in 0.23s =========================
```
