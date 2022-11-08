from math import sqrt, isclose


def calculate_pi(n: int):
    """
    Approximate pi using the formula: pi**2 / 6 = sum of 1/k**2 for k = 1 to n,
    rewritten as: pi = (6 * sum of 1/k**2 for k = 1 to n)**0.5
    """
    sum = 0

    for i in range(1, n + 1):
        sum += 1 / (i**2)

    return sqrt(sum * 6)


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(calculate_pi(-3), 0.0, abs_tol=eps, rel_tol=eps)
    assert isclose(calculate_pi(1), 2.44948, rel_tol=eps)
    assert isclose(calculate_pi(7), 3.01177, rel_tol=eps)
    assert isclose(calculate_pi(1000), 3.14063, rel_tol=eps)
    assert isclose(calculate_pi(10000), 3.14149, rel_tol=eps)
