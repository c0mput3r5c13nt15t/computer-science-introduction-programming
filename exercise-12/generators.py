from typing import Callable, Generator, Iterator


# differentiate from exercise-11/integral.py
def differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float]:
    return lambda x: (f(x + h) - f(x - h)) / (2 * h)


def newton(f: Callable[[float], float], x: float) -> Generator[float, None, None]:
    while True:
        x = x - f(x) / differentiate(f, 0.0001)(x)
        yield x


def generate_target(iterable: Iterator[float], f: Callable[[float], float], target: float) -> Generator[float, None, None]:
    x = next(iterable)
    yield x
    while abs(f(x)) >= target:
        x = next(iterable)
        yield x


def arithmetic_mean(iterable: Iterator[float]) -> Generator[float, None, None]:
    x = next(iterable)
    n = 1
    yield x
    for next_x in iterable:
        x = (n * x + next_x) / (n + 1)
        n += 1
        yield x


def map13(iterable: Iterator[int]) -> Iterator[int]:
    return map(lambda x: x % 13, iterable)


def filter57(iterable: Iterator[int]) -> Iterator[int]:
    return filter(lambda x: x % 5 == 0 or x % 7 == 0, iterable)


if __name__ == "__main__":
    # generator = newton(lambda x: 2 * x + 1, 3)
    # for i in range(3):
    #     print(next(generator))

    def f(x): return 2 * x + 1
    generator = newton(f, 3)

    assert f(list(generate_target(generator, f, 1e-12))[-1]) < 1e-12

    assert list(arithmetic_mean(iter(range(0, 21, 4)))) == [
        0.0, 2.0, 4.0, 6.0, 8.0, 10.0]

    input_iterator = iter(range(0, 26, 5))
    assert list(map13(input_iterator)) == [0, 5, 10, 2, 7, 12]

    input_iterator = iter(range(20))
    assert list(filter57(input_iterator)) == [0, 5, 7, 10, 14, 15]
