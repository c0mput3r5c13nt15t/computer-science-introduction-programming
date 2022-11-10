def is_prime(x: int, ps: list[int]) -> bool:
    """
    Returns True if x is prime, False otherwise.
    """
    for p in ps:
        if x % p == 0:
            return False
    return True


def primes(n: int) -> list[int]:
    """
    Returns all prime numbers up to n.
    """

    ps = []
    x = 2
    for i in range(n - 1):
        if is_prime(x, ps):
            ps += [x]
        x += 1
    return ps


if __name__ == "__main__":
    assert primes(1) == []
    assert primes(3) == [2, 3]
    assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
