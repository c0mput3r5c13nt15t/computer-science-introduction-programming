from math import isclose


def reverse(list: list):
    new_list = []
    for i in list:
        new_list = [i] + new_list
    return new_list


def only_positive(list: list[int]):
    new_list = []

    for num in list:
        if num > 0:
            new_list += [num]

    return new_list


def average(list: list[float]):
    if len(list) == 0:
        return 0
    return sum(list) / len(list)


if __name__ == "__main__":
    # Test the reverse function
    assert reverse([]) == []
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    # Test the only_positive function
    assert only_positive([]) == []
    assert only_positive([1, 2, 3]) == [1, 2, 3]
    assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]

    # Test the average function
    eps = 1e-4
    assert isclose(average([]), 0.0, abs_tol=eps, rel_tol=eps)
    assert isclose(average([1.0]), 1.0, rel_tol=eps)
    assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol=eps)
