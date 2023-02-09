# exercise-14 (19 / 20)

### Aufgabe 1: Sequence (9/10)
Typannotationen fehlen (-1P)
### Aufgabe 2: Dictionaries & Sets (10/10)
Sehr schön
### Aufgabe 3: Strings (20/20)
Funktioniert auch, aber in der Klausur am besten auch die Hinweise beachten. Meistens geht es dann einfacher.
### Aufgabe 4: Dataclasses (15/20)
* a) Gleiche Nachnamen werden nicht richtig behandelt (-1P)
* b) Funktioniert auch, aber MouseCLick und KeyPress sollten auch definiert werden (-1P)
* c) Grenzen für x und y werden weder bei der Initialisierung noch bei move() überprüft (-3P)
### Aufgabe 5: Tests (10/10)
Ein assert pro return hätte auch genügt
### Aufgabe 6: Rekursion (14/15)
* a) Typannotation stimmt nicht, da tree auch None sein kann (also vom Typ tree) (-1P)
* b) Hier selbes, auch wenn du es manuell gelöst hast
### Aufgabe 7: Generatoren (20/20)
Sehr schön

### Aufgabe 8: Funktionale Programmierung (15/15)
Auch sehr gut

### Gesamt
(113/120) -> (17/18)

### NOTES (2/2)
Die Probeklausur ist sowohl vom Umfang als auch der Schwierigkeit nah an der richtigen Klausur. Das Tempo der Onlinesimulation kann ich nicht einschätzen, aber bis jetzt hat es nie solche Probleme bei den Poolrechnern gegeben.
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
collecting ... collected 140 items

test_14.py::test_ex1_sequence_count_iterations_typing FAILED
test_14.py::test_ex1_sequence_count_iterations PASSED
test_14.py::test_ex1_sequence_count_iterations_zero PASSED
test_14.py::test_ex2_dicts_compose_typing PASSED
test_14.py::test_ex2_dicts_compose PASSED
test_14.py::test_ex2_dicts_compose_prof_no_courses PASSED
test_14.py::test_ex2_dicts_compose_course_no_students PASSED
test_14.py::test_ex3_strings_is_list_of_int_typing PASSED
test_14.py::test_ex3_strings_is_list_of_int x [100,-44,0]
x [123,456,]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_empty_string x 
PASSED
test_14.py::test_ex3_strings_is_list_of_int_only_bracket_left x [
PASSED
test_14.py::test_ex3_strings_is_list_of_int_only_bracket_right x ]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_empty_list x []
PASSED
test_14.py::test_ex3_strings_is_list_of_int_starts_without_bracket x 23]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_ends_without_bracket x [23
PASSED
test_14.py::test_ex3_strings_is_list_of_int_comma_at_start x [,34]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_comma_at_end x [34,]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_other_seperator x [34.645]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_no_spaces x [34, 645]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_only_minus x [-]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_single_number x 24
PASSED
test_14.py::test_ex3_strings_is_list_of_int_single_number_in_list x [24]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_double_minus x [--24]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_no_plus x [+24]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_only_positive x [1,2,3,4,5,6]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_only_negative x [-6,-5,-4,-3,-2,-1]
PASSED
test_14.py::test_ex3_strings_is_list_of_int_mixed x [-30,-29,28,-27,-26,-25,-24,-23,-22,21,-20,-19,-18,-17,-16,-15,14,-13,-12,-11,-10,-9,-8,7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,-7,8,9,10,11,12,13,-14,15,16,17,18,19,20,-21,22,23,24,25,26,27,-28,29]
PASSED
test_14.py::test_ex4_classes_name_typing PASSED
test_14.py::test_ex4_classes_name PASSED
test_14.py::test_ex4_classes_name_has_getter_surname PASSED
test_14.py::test_ex4_classes_name_has_getter_prename PASSED
test_14.py::test_ex4_classes_name_has_setter_surname PASSED
test_14.py::test_ex4_classes_name_has_setter_prename PASSED
test_14.py::test_ex4_classes_name___lt___typing FAILED
test_14.py::test_ex4_classes_name___lt__ FAILED
test_14.py::test_ex4_classes_mouse_click_does_not_inherit FAILED
test_14.py::test_ex4_classes_mouse_click_typing SKIPPED (must not annotate a non dataclass)
test_14.py::test_ex4_classes_mouse_click FAILED
test_14.py::test_ex4_classes_mouse_click_has_getter_x FAILED
test_14.py::test_ex4_classes_mouse_click_has_getter_y FAILED
test_14.py::test_ex4_classes_mouse_click_has_setter_x FAILED
test_14.py::test_ex4_classes_mouse_click_has_setter_y FAILED
test_14.py::test_ex4_classes_key_press_does_not_inherit FAILED
test_14.py::test_ex4_classes_key_press_typing SKIPPED (must not annotate a non dataclass)
test_14.py::test_ex4_classes_key_press FAILED
test_14.py::test_ex4_classes_key_press_has_getter_key FAILED
test_14.py::test_ex4_classes_key_press_has_setter_key FAILED
test_14.py::test_ex4_classes_event_is_union_type FAILED
test_14.py::test_ex4_classes_log_event_typing PASSED
test_14.py::test_ex4_classes_log_event_uses_match FAILED
test_14.py::test_ex4_classes_log_event_mouse_click FAILED
test_14.py::test_ex4_classes_log_event_mouse_click2 FAILED
test_14.py::test_ex4_classes_log_event_key_press FAILED
test_14.py::test_ex4_classes_log_event_key_press2 FAILED
test_14.py::test_ex4_classes_game_object_does_not_inherit PASSED
test_14.py::test_ex4_classes_game_object_typing PASSED
test_14.py::test_ex4_classes_game_object PASSED
test_14.py::test_ex4_classes_game_object_allow_zero_x PASSED
test_14.py::test_ex4_classes_game_object_reject_negative_x FAILED
test_14.py::test_ex4_classes_game_object_allow_zero_y PASSED
test_14.py::test_ex4_classes_game_object_reject_negative_y FAILED
test_14.py::test_ex4_classes_game_object_has_getter_x PASSED
test_14.py::test_ex4_classes_game_object_has_getter_y PASSED
test_14.py::test_ex4_classes_game_object_has_setter_x PASSED
test_14.py::test_ex4_classes_game_object_has_setter_y PASSED
test_14.py::test_ex4_classes_game_object_move_typing PASSED
test_14.py::test_ex4_classes_game_object_move_add_x PASSED
test_14.py::test_ex4_classes_game_object_move_subtract_x PASSED
test_14.py::test_ex4_classes_game_object_move_zero_x PASSED
test_14.py::test_ex4_classes_game_object_move_add_y PASSED
test_14.py::test_ex4_classes_game_object_move_subtract_y PASSED
test_14.py::test_ex4_classes_game_object_move_zero_y PASSED
test_14.py::test_ex4_classes_game_object_move_allow_zero_x PASSED
test_14.py::test_ex4_classes_game_object_move_reject_negative_x FAILED
test_14.py::test_ex4_classes_game_object_move_allow_zero_y PASSED
test_14.py::test_ex4_classes_game_object_move_reject_negative_y FAILED
test_14.py::test_ex4_classes_player_does_inherit PASSED
test_14.py::test_ex4_classes_player_typing PASSED
test_14.py::test_ex4_classes_player___post_init___calls_super FAILED
test_14.py::test_ex4_classes_player PASSED
test_14.py::test_ex4_classes_player_allow_zero_health PASSED
test_14.py::test_ex4_classes_player_reject_negative_health PASSED
test_14.py::test_ex4_classes_player_has_getter_health PASSED
test_14.py::test_ex4_classes_player_has_setter_health PASSED
test_14.py::test_ex4_classes_player_does_inherit_move PASSED
test_14.py::test_ex5_tests_has_exactly_4_tests PASSED
test_14.py::test_ex5_tests_defined_tests_pass PASSED
test_14.py::test_ex5_tests_tests_first_return PASSED
test_14.py::test_ex5_tests_tests_second_return PASSED
test_14.py::test_ex5_tests_tests_third_return PASSED
test_14.py::test_ex5_tests_tests_fourth_return PASSED
test_14.py::test_ex6_trees_mark_at_path_typing FAILED
test_14.py::test_ex6_trees_mark_at_path PASSED
test_14.py::test_ex6_trees_mark_at_path_accepts_empty_tree FAILED
test_14.py::test_ex6_trees_mark_at_path_accepts_empty_path PASSED
test_14.py::test_ex6_trees_mark_at_path_can_nest_up_to_500_left PASSED
test_14.py::test_ex6_trees_mark_at_path_can_nest_up_to_500_right PASSED
test_14.py::test_ex6_trees_mark_at_path_can_nest_up_to_200_alternating PASSED
test_14.py::test_ex6_trees_mark_at_path_can_nest_up_to_300_right_double_left PASSED
test_14.py::test_ex6_trees_paths_typing FAILED
test_14.py::test_ex6_trees_paths PASSED
test_14.py::test_ex6_trees_paths_only_left PASSED
test_14.py::test_ex6_trees_paths_saturated_tree PASSED
test_14.py::test_ex6_trees_paths_only_right PASSED
test_14.py::test_ex6_trees_paths_alternate PASSED
test_14.py::test_ex6_trees_paths_left_double_right PASSED
test_14.py::test_ex7_generators_no_imports PASSED
test_14.py::test_ex7_generators_my_chain PASSED
test_14.py::test_ex7_generators_my_chain_ys_empty PASSED
test_14.py::test_ex7_generators_my_chain_xs_empty PASSED
test_14.py::test_ex7_generators_my_chain_empty PASSED
test_14.py::test_ex7_generators_my_chain_xs_infinite PASSED
test_14.py::test_ex7_generators_my_chain_ys_infinite PASSED
test_14.py::test_ex7_generators_dup PASSED
test_14.py::test_ex7_generators_dup_0 PASSED
test_14.py::test_ex7_generators_dup_negative PASSED
test_14.py::test_ex7_generators_dup_finite PASSED
test_14.py::test_ex7_generators_dup_infinite PASSED
test_14.py::test_ex7_generators_compare_example PASSED
test_14.py::test_ex7_generators_compare_xs_empty PASSED
test_14.py::test_ex7_generators_compare_ys_empty FAILED
test_14.py::test_ex7_generators_compare_empty PASSED
test_14.py::test_ex7_generators_compare_equal FAILED
test_14.py::test_ex8_fp_times_2_is_lambda_definition PASSED
test_14.py::test_ex8_fp_times_2 PASSED
test_14.py::test_ex8_fp_times_2_different_input PASSED
test_14.py::test_ex8_fp_times_2_different_function PASSED
test_14.py::test_ex8_fp_map_matrix_is_lambda_definition PASSED
test_14.py::test_ex8_fp_map_matrix PASSED
test_14.py::test_ex8_fp_map_matrix_empty_matrix PASSED
test_14.py::test_ex8_fp_map_matrix_different_function PASSED
test_14.py::test_ex8_fp_map_matrix_does_not_use_map PASSED
test_14.py::test_ex8_fp_map_matrix_does_not_use_list PASSED
test_14.py::test_ex8_fp_map_matrix_2_is_lambda_definition PASSED
test_14.py::test_ex8_fp_map_matrix_2 PASSED
test_14.py::test_ex8_fp_map_matrix_2_empty_matrix PASSED
test_14.py::test_ex8_fp_map_matrix_2_different_function PASSED
test_14.py::test_ex8_fp_map_matrix_2_uses_map PASSED
test_14.py::test_ex8_fp_map_matrix_2_uses_list PASSED
test_14.py::test_ex8_fp_map_matrix_2_uses_lambda PASSED

=================================== FAILURES ===================================
__________________ test_ex1_sequence_count_iterations_typing ___________________

    def test_ex1_sequence_count_iterations_typing():
>       check_typing(
            count_iterations,
            return_annotation=int,
            named={
                "n": int,
                "a": int
            }
        )

test_14.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests_lib.py:275: in check_typing
    check_typing_multi(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

function = <function count_iterations at 0x7f326d2613f0>
return_annotation = (<class 'int'>,), positional = []
named = {'a': (<class 'int'>,), 'n': (<class 'int'>,)}

    def check_typing_multi(function: Callable | type,
                           return_annotation: Optional[tuple[Any, ...]] = None,
                           positional: list[tuple[Any, ...]] = [],
                           named: dict[str, tuple[Any, ...]] = {}):
        given = function.__annotations__
        if return_annotation is not None:
>           assert given.pop('return', None) in return_annotation, 'wrong return type'
E           AssertionError: wrong return type

tests_lib.py:257: AssertionError
_____________________ test_ex4_classes_name___lt___typing ______________________

    def test_ex4_classes_name___lt___typing():
        try:
>           check_typing(
                Name.__lt__,
                return_annotation=bool,
                positional=['Name']
            )

test_14.py:248: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests_lib.py:275: in check_typing
    check_typing_multi(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

function = <function Name.__lt__ at 0x7f326d262560>
return_annotation = (<class 'bool'>,), positional = [('Name',)], named = {}

    def check_typing_multi(function: Callable | type,
                           return_annotation: Optional[tuple[Any, ...]] = None,
                           positional: list[tuple[Any, ...]] = [],
                           named: dict[str, tuple[Any, ...]] = {}):
        given = function.__annotations__
        if return_annotation is not None:
>           assert given.pop('return', None) in return_annotation, 'wrong return type'
E           AssertionError: wrong return type

tests_lib.py:257: AssertionError
_________________________ test_ex4_classes_name___lt__ _________________________

    def test_ex4_classes_name___lt__():
        name1 = Name(surname="Müller", prename="Anton")
        name2 = Name(surname="Meier", prename="Ute")
        name3 = Name(surname="Meier", prename="Frank")
    
        assert name2 < name1
>       assert name3 < name2
E       AssertionError: assert Name(prename='Frank', surname='Meier') < Name(prename='Ute', surname='Meier')

test_14.py:267: AssertionError
________________ test_ex4_classes_mouse_click_does_not_inherit _________________

    def test_ex4_classes_mouse_click_does_not_inherit():
>       check_does_not_inherit(MouseClick)

test_14.py:281: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_class = <class 'test_14.MouseClick'>

    def check_does_not_inherit(_class: type):
>       assert _class.__weakref__.__qualname__ == f"{_class.__qualname__}.__weakref__"
E       AssertionError

tests_lib.py:299: AssertionError
_________________________ test_ex4_classes_mouse_click _________________________

    def test_ex4_classes_mouse_click():
>       MouseClick(3, 2)

test_14.py:299: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.MouseClick object at 0x7f326d3536a0>, args = (3, 2), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
__________________ test_ex4_classes_mouse_click_has_getter_x ___________________

    def test_ex4_classes_mouse_click_has_getter_x():
>       mouse_click = MouseClick(3, 2)

test_14.py:303: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.MouseClick object at 0x7f326d28c5e0>, args = (3, 2), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
__________________ test_ex4_classes_mouse_click_has_getter_y ___________________

    def test_ex4_classes_mouse_click_has_getter_y():
>       mouse_click = MouseClick(3, 2)

test_14.py:308: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.MouseClick object at 0x7f326d05cd90>, args = (3, 2), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
__________________ test_ex4_classes_mouse_click_has_setter_x ___________________

    def test_ex4_classes_mouse_click_has_setter_x():
>       mouse_click = MouseClick(3, 2)

test_14.py:313: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.MouseClick object at 0x7f326d98abf0>, args = (3, 2), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
__________________ test_ex4_classes_mouse_click_has_setter_y ___________________

    def test_ex4_classes_mouse_click_has_setter_y():
>       mouse_click = MouseClick(3, 2)

test_14.py:320: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.MouseClick object at 0x7f326d352050>, args = (3, 2), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
_________________ test_ex4_classes_key_press_does_not_inherit __________________

    def test_ex4_classes_key_press_does_not_inherit():
>       check_does_not_inherit(KeyPress)

test_14.py:334: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_class = <class 'test_14.KeyPress'>

    def check_does_not_inherit(_class: type):
>       assert _class.__weakref__.__qualname__ == f"{_class.__qualname__}.__weakref__"
E       AssertionError

tests_lib.py:299: AssertionError
__________________________ test_ex4_classes_key_press __________________________

    def test_ex4_classes_key_press():
>       KeyPress("a")

test_14.py:351: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.KeyPress object at 0x7f326d281540>, args = ('a',), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
__________________ test_ex4_classes_key_press_has_getter_key ___________________

    def test_ex4_classes_key_press_has_getter_key():
>       key_press = KeyPress("a")

test_14.py:355: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.KeyPress object at 0x7f326d2b8d30>, args = ('a',), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
__________________ test_ex4_classes_key_press_has_setter_key ___________________

    def test_ex4_classes_key_press_has_setter_key():
>       key_press = KeyPress("a")

test_14.py:360: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_14.KeyPress object at 0x7f326d28d120>, args = ('a',), kwargs = {}

    def __init__(self, *args, **kwargs):
>       raise NotImplementedError
E       NotImplementedError

tests_lib.py:49: NotImplementedError
_____________________ test_ex4_classes_event_is_union_type _____________________

    def test_ex4_classes_event_is_union_type():
>       assert Event == MouseClick | KeyPress
E       assert Event == (MouseClick | KeyPress)

test_14.py:373: AssertionError
____________________ test_ex4_classes_log_event_uses_match _____________________

    def test_ex4_classes_log_event_uses_match():
>       check_source_matches(
            "ex4_classes.py",
            re.compile(
                r"def\s+log_event.*match.*case\s+MouseClick.*case\s+KeyPress",
                re.DOTALL
            )
        )

test_14.py:387: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = 'ex4_classes.py'
regex = re.compile('def\\s+log_event.*match.*case\\s+MouseClick.*case\\s+KeyPress', re.DOTALL)

    def check_source_matches(filename: str, regex: re.Pattern):
>       assert __get_source_match(filename, regex) is not None
E       AssertionError

tests_lib.py:342: AssertionError
____________________ test_ex4_classes_log_event_mouse_click ____________________

    def test_ex4_classes_log_event_mouse_click():
        with IOMock("ex4_classes") as io:
>           MouseClick = io.get("MouseClick")

test_14.py:398: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = IOMock(module_name='ex4_classes', module_local_name=None, _IOMock__print_buffer=[], _IOMock__input_buffer=[], _IOMock_..._classes' from '/mnt/c/Users/kraut/Documents/7. Semester/Info Tutorat/2022WS-EiP/m172947g/exercise-14/ex4_classes.py'>)
name = 'MouseClick', default = None

    def get(self, name: str, default: Any = None) -> Any:
        module = self.module
        if module is None:
            return default
        try:
>           return self.__module.__dict__[name]
E           KeyError: 'MouseClick'

tests_lib.py:202: KeyError
___________________ test_ex4_classes_log_event_mouse_click2 ____________________

    def test_ex4_classes_log_event_mouse_click2():
        with IOMock("ex4_classes") as io:
>           MouseClick = io.get("MouseClick")

test_14.py:405: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = IOMock(module_name='ex4_classes', module_local_name=None, _IOMock__print_buffer=[], _IOMock__input_buffer=[], _IOMock_..._classes' from '/mnt/c/Users/kraut/Documents/7. Semester/Info Tutorat/2022WS-EiP/m172947g/exercise-14/ex4_classes.py'>)
name = 'MouseClick', default = None

    def get(self, name: str, default: Any = None) -> Any:
        module = self.module
        if module is None:
            return default
        try:
>           return self.__module.__dict__[name]
E           KeyError: 'MouseClick'

tests_lib.py:202: KeyError
_____________________ test_ex4_classes_log_event_key_press _____________________

    def test_ex4_classes_log_event_key_press():
        with IOMock("ex4_classes") as io:
>           KeyPress = io.get("KeyPress")

test_14.py:412: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = IOMock(module_name='ex4_classes', module_local_name=None, _IOMock__print_buffer=[], _IOMock__input_buffer=[], _IOMock_..._classes' from '/mnt/c/Users/kraut/Documents/7. Semester/Info Tutorat/2022WS-EiP/m172947g/exercise-14/ex4_classes.py'>)
name = 'KeyPress', default = None

    def get(self, name: str, default: Any = None) -> Any:
        module = self.module
        if module is None:
            return default
        try:
>           return self.__module.__dict__[name]
E           KeyError: 'KeyPress'

tests_lib.py:202: KeyError
____________________ test_ex4_classes_log_event_key_press2 _____________________

    def test_ex4_classes_log_event_key_press2():
        with IOMock("ex4_classes") as io:
>           KeyPress = io.get("KeyPress")

test_14.py:419: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = IOMock(module_name='ex4_classes', module_local_name=None, _IOMock__print_buffer=[], _IOMock__input_buffer=[], _IOMock_..._classes' from '/mnt/c/Users/kraut/Documents/7. Semester/Info Tutorat/2022WS-EiP/m172947g/exercise-14/ex4_classes.py'>)
name = 'KeyPress', default = None

    def get(self, name: str, default: Any = None) -> Any:
        module = self.module
        if module is None:
            return default
        try:
>           return self.__module.__dict__[name]
E           KeyError: 'KeyPress'

tests_lib.py:202: KeyError
________________ test_ex4_classes_game_object_reject_negative_x ________________

    def test_ex4_classes_game_object_reject_negative_x():
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

test_14.py:461: Failed
________________ test_ex4_classes_game_object_reject_negative_y ________________

    def test_ex4_classes_game_object_reject_negative_y():
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

test_14.py:470: Failed
_____________ test_ex4_classes_game_object_move_reject_negative_x ______________

    def test_ex4_classes_game_object_move_reject_negative_x():
        game_object = GameObject(6, 9)
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

test_14.py:552: Failed
_____________ test_ex4_classes_game_object_move_reject_negative_y ______________

    def test_ex4_classes_game_object_move_reject_negative_y():
        game_object = GameObject(6, 9)
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

test_14.py:564: Failed
______________ test_ex4_classes_player___post_init___calls_super _______________

    def test_ex4_classes_player___post_init___calls_super():
>       check_source_matches(
            "ex4_classes.py",
            re.compile(
                r"Player.*def\s+__post_init__.*super\(\).__post_init__\(\)",
                re.DOTALL
            )
        )

test_14.py:594: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = 'ex4_classes.py'
regex = re.compile('Player.*def\\s+__post_init__.*super\\(\\).__post_init__\\(\\)', re.DOTALL)

    def check_source_matches(filename: str, regex: re.Pattern):
>       assert __get_source_match(filename, regex) is not None
E       AssertionError

tests_lib.py:342: AssertionError
______________________ test_ex6_trees_mark_at_path_typing ______________________

    def test_ex6_trees_mark_at_path_typing():
>       check_typing(
            mark_at_path,
            return_annotation=Optional[str],
            named={
                "tree": Tree,
                "path": str
            }
        )

test_14.py:869: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests_lib.py:275: in check_typing
    check_typing_multi(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

function = <function mark_at_path at 0x7f326cff6950>
return_annotation = (typing.Optional[str],), positional = []
named = {'path': (<class 'str'>,), 'tree': (typing.Optional[ex6_trees.Node],)}

    def check_typing_multi(function: Callable | type,
                           return_annotation: Optional[tuple[Any, ...]] = None,
                           positional: list[tuple[Any, ...]] = [],
                           named: dict[str, tuple[Any, ...]] = {}):
        given = function.__annotations__
        if return_annotation is not None:
            assert given.pop('return', None) in return_annotation, 'wrong return type'
        else:
            if given.get('return', None) is None:
                given.pop('return', None)
            assert 'return' not in given.keys(), 'wrong return type'
        for param, expected in named.items():
            annotation = given.get(param, None)
>           assert annotation in expected or str(annotation) in map(str, expected), f'wrong {param} type, one of {expected} expected, but got {annotation}'
E           AssertionError: wrong tree type, one of (typing.Optional[ex6_trees.Node],) expected, but got <class 'ex6_trees.Node'>

tests_lib.py:264: AssertionError
________________ test_ex6_trees_mark_at_path_accepts_empty_tree ________________

    def test_ex6_trees_mark_at_path_accepts_empty_tree():
>       assert mark_at_path(None, "") is None

test_14.py:895: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

tree = None, path = ''

    def mark_at_path(tree: Node, path: str) -> str | None:
        current_node = tree
    
        if not path:
>           return current_node.mark
E           AttributeError: 'NoneType' object has no attribute 'mark'

ex6_trees.py:23: AttributeError
_________________________ test_ex6_trees_paths_typing __________________________

    def test_ex6_trees_paths_typing():
>       check_typing(
            paths,
            return_annotation=list[str],
            named={
                "tree": Tree
            }
        )

test_14.py:955: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests_lib.py:275: in check_typing
    check_typing_multi(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

function = <function paths at 0x7f326cff7400>, return_annotation = (list[str],)
positional = [], named = {'tree': (typing.Optional[ex6_trees.Node],)}

    def check_typing_multi(function: Callable | type,
                           return_annotation: Optional[tuple[Any, ...]] = None,
                           positional: list[tuple[Any, ...]] = [],
                           named: dict[str, tuple[Any, ...]] = {}):
        given = function.__annotations__
        if return_annotation is not None:
            assert given.pop('return', None) in return_annotation, 'wrong return type'
        else:
            if given.get('return', None) is None:
                given.pop('return', None)
            assert 'return' not in given.keys(), 'wrong return type'
        for param, expected in named.items():
            annotation = given.get(param, None)
>           assert annotation in expected or str(annotation) in map(str, expected), f'wrong {param} type, one of {expected} expected, but got {annotation}'
E           AssertionError: wrong tree type, one of (typing.Optional[ex6_trees.Node],) expected, but got ex6_trees.Node | None

tests_lib.py:264: AssertionError
_____________________ test_ex7_generators_compare_ys_empty _____________________

    def test_ex7_generators_compare_ys_empty():
        compare_gen = compare(FibIteratorClass(5), [])
        with pytest.raises(StopIteration):
>           next(compare_gen)

test_14.py:1167: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

xs = FibIteratorClass(max_n=5, prev=1, prev_prev=0, n=0), ys = []

    def compare(xs, ys):
>       for i in range(min(len(xs), len(ys))):
E       TypeError: object of type 'FibIteratorClass' has no len()

ex7_generators.py:24: TypeError
______________________ test_ex7_generators_compare_equal _______________________

    def test_ex7_generators_compare_equal():
        compare_gen = compare(FibIteratorClass(5), infinite_generator())
>       assert list(compare_gen) == [0, 1, 4, 9, 16]

test_14.py:1178: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

xs = FibIteratorClass(max_n=5, prev=1, prev_prev=0, n=0)
ys = <generator object infinite_generator at 0x7f326d0d8660>

    def compare(xs, ys):
>       for i in range(min(len(xs), len(ys))):
E       TypeError: object of type 'FibIteratorClass' has no len()

ex7_generators.py:24: TypeError
=========================== short test summary info ============================
FAILED test_14.py::test_ex1_sequence_count_iterations_typing - AssertionError...
FAILED test_14.py::test_ex4_classes_name___lt___typing - AssertionError: wron...
FAILED test_14.py::test_ex4_classes_name___lt__ - AssertionError: assert Name...
FAILED test_14.py::test_ex4_classes_mouse_click_does_not_inherit - AssertionE...
FAILED test_14.py::test_ex4_classes_mouse_click - NotImplementedError
FAILED test_14.py::test_ex4_classes_mouse_click_has_getter_x - NotImplemented...
FAILED test_14.py::test_ex4_classes_mouse_click_has_getter_y - NotImplemented...
FAILED test_14.py::test_ex4_classes_mouse_click_has_setter_x - NotImplemented...
FAILED test_14.py::test_ex4_classes_mouse_click_has_setter_y - NotImplemented...
FAILED test_14.py::test_ex4_classes_key_press_does_not_inherit - AssertionError
FAILED test_14.py::test_ex4_classes_key_press - NotImplementedError
FAILED test_14.py::test_ex4_classes_key_press_has_getter_key - NotImplemented...
FAILED test_14.py::test_ex4_classes_key_press_has_setter_key - NotImplemented...
FAILED test_14.py::test_ex4_classes_event_is_union_type - assert Event == (Mo...
FAILED test_14.py::test_ex4_classes_log_event_uses_match - AssertionError
FAILED test_14.py::test_ex4_classes_log_event_mouse_click - KeyError: 'MouseC...
FAILED test_14.py::test_ex4_classes_log_event_mouse_click2 - KeyError: 'Mouse...
FAILED test_14.py::test_ex4_classes_log_event_key_press - KeyError: 'KeyPress'
FAILED test_14.py::test_ex4_classes_log_event_key_press2 - KeyError: 'KeyPress'
FAILED test_14.py::test_ex4_classes_game_object_reject_negative_x - Failed: D...
FAILED test_14.py::test_ex4_classes_game_object_reject_negative_y - Failed: D...
FAILED test_14.py::test_ex4_classes_game_object_move_reject_negative_x - Fail...
FAILED test_14.py::test_ex4_classes_game_object_move_reject_negative_y - Fail...
FAILED test_14.py::test_ex4_classes_player___post_init___calls_super - Assert...
FAILED test_14.py::test_ex6_trees_mark_at_path_typing - AssertionError: wrong...
FAILED test_14.py::test_ex6_trees_mark_at_path_accepts_empty_tree - Attribute...
FAILED test_14.py::test_ex6_trees_paths_typing - AssertionError: wrong tree t...
FAILED test_14.py::test_ex7_generators_compare_ys_empty - TypeError: object o...
FAILED test_14.py::test_ex7_generators_compare_equal - TypeError: object of t...
================== 29 failed, 109 passed, 2 skipped in 0.94s ===================
```
