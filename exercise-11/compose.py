from typing import Callable


def compose(f: Callable[[int], int], g: Callable[[int, int], int]) -> Callable[[int, int], int]:
    return lambda x, y: f(g(x, y))


if __name__ == "__main__":
    def inc(x): return x + 1
    def mul(x, y): return x * y
    assert compose(inc, mul)(4, 2) == 9
