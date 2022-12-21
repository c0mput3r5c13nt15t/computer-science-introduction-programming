def update_points(original: dict[str, int], changes: dict[str, int]):
    for name, points in changes.items():
        if name not in original:
            raise KeyError(f'{name} wurde nicht gefunden')

        new_points = original[name] + points

        if new_points < 0 or new_points > 120:
            raise ValueError(
                'Die Gesamtpunktzahl muss zwischen 0 und 120 liegen')

        original[name] = new_points


def compute_grade_simple(points: int, max_points: int, pass_points: int) -> int:
    if points > pass_points + 0.75 * (max_points - pass_points):
        return 1
    elif points > pass_points + 0.5 * (max_points - pass_points):
        return 2
    elif points > pass_points + 0.25 * (max_points - pass_points):
        return 3
    elif points > pass_points:
        return 4
    else:  # points <= pass_points
        return 5


def failure_rate(student_points: dict[str, int], max_points: int, pass_points: int) -> float:
    failure_rate = 0
    for _, points in student_points.items():
        if points < pass_points:
            failure_rate += 1

    return failure_rate / len(student_points)


def calculate_pass_points(student_points: dict[str, int], max_points: int) -> int:
    pass_points = max_points // 2

    while failure_rate(student_points, max_points, pass_points) > 0.4:
        pass_points -= 1

    return pass_points


def compute_grade(student_points: dict[str, int], max_points: int, student_name: str) -> int:
    if student_name not in student_points:
        raise KeyError(f'{student_name} wurde nicht gefunden')

    pass_points = calculate_pass_points(student_points, max_points)

    return compute_grade_simple(student_points[student_name], max_points, pass_points)


def cluster_by_grade(student_points: dict[str, int], max_points: int) -> dict[int, list[str]]:
    pass_points = calculate_pass_points(student_points, max_points)

    grades = {}
    for name, points in student_points.items():
        grade = compute_grade_simple(points, max_points, pass_points)

        if grade not in grades:
            grades[grade] = []

        grades[grade] += [name]

    return grades


if __name__ == '__main__':
    student_points = {"Adam": 63, "John": 112, "Donald": 43}
    changes = {"Adam": 3, "John": -7}
    update_points(student_points, changes)
    print(student_points)
    print(compute_grade(student_points, 120, "Adam"))
    student_points = {"Mira": 80, "Olivia": 95, "Emily": 83}
    print(cluster_by_grade(student_points, 120))
