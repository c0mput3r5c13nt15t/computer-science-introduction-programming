# Aufgabe 2 (Dictionaries und Sets) ###########################################

def compose(prof_to_courses: dict[str, set[str]], course_to_students: dict[str, set[str]]) -> dict[str, set[str]]:
    prof_to_students = {}
    for prof in prof_to_courses.keys():
        students = set()
        for course in prof_to_courses[prof]:
            for student in course_to_students[course]:
                students.add(student)
        prof_to_students[prof] = students
    return prof_to_students


if __name__ == "__main__":
    prof_to_courses = {
        "Prof A": {"Course A", "Course B"},
        "Prof B": {"Course B", "Course C"},
    }
    course_to_students = {
        "Course A": {"Student A", "Student B"},
        "Course B": {"Student B", "Student C"},
        "Course C": {"Student D", "Student E"},
    }

    assert compose(prof_to_courses, course_to_students) == {
        "Prof A": {"Student A", "Student B", "Student C"},
        "Prof B": {"Student B", "Student C", "Student D", "Student E"},
    }
