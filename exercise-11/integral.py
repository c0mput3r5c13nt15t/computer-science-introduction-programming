import math
from typing import Callable


def differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float]:
    return lambda x: (f(x + h) - f(x - h)) / (2 * h)


def integrate(f: Callable[[float], float], n: int) -> Callable[[float, float], float]:
    # Calculate the approximate value of the integral using Simpson's rule
    def simpson(a: float, b: float) -> float:
        h = (b - a) / n
        def xi(i: int): return a + i * h

        def si(i: int): return h / 6 * (f(xi(i)) + 4 *
                                        f((xi(i) + xi(i + 1)) / 2) + f(xi(i + 1)))

        return sum(map(si, range(0, n)))
    return simpson
