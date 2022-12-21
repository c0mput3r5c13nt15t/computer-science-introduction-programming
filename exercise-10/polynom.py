from polynom_test import test_many_cracker_n


def crack_1(f) -> list[int]:
    a0 = f(0)
    a1 = f(1) - a0
    return [a0, a1]


def crack_2(f) -> list[int]:
    a0 = f(0)
    a2 = (f(1) + f(-1) - 2 * a0) // 2  # Assumption: a2 is an integer
    a1 = f(1) - a0 - a2

    return [a0, a1, a2]


def crack_3(f) -> list[int]:
    a0 = f(0)
    a2 = (f(1) + f(-1) - 2 * a0) // 2  # Assumption: a2 is an integer
    # Assumption: a3 is an integer
    a3 = (f(2) + 2 * f(-1) - 3 * a0 - 6 * a2) // 6
    a1 = f(1) - a0 - a2 - a3

    return [a0, a1, a2, a3]


def f10(x: int) -> int:
    return 1 + 2 * x


def f11(x: int) -> int:
    return -1 + 3 * x


def f20(x: int) -> int:
    return 1 + 2 * x + x * x


def f21(x: int) -> int:
    return -1 - 4 * x + 2 * x * x


def f22(x: int) -> int:
    return (x + 1) * (x - 1)


def f30(x: int) -> int:
    return x * (x + 10) * (x - 5)


if __name__ == '__main__':
    test_many_cracker_n(1, crack_1)
    test_many_cracker_n(2, crack_2)
    test_many_cracker_n(3, crack_3)
