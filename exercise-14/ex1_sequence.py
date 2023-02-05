# Aufgabe 1 (Sequence) ########################################################

def next_n(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 9 * n + 3


def count_iterations(n, a):
    i = 0
    while n < a:
        i += 1
        n = next_n(n)
    return i


if __name__ == "__main__":
    assert count_iterations(3, 100) == 3
