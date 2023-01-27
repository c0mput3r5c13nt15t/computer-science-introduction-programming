from typing import Callable
from functools import partial


def suppress(f: Callable, ignore: tuple) -> Callable:
    def g():
        try:
            return f()
        except Exception as error:
            if isinstance(error, ignore):
                return
            raise
    return g


if __name__ == "__main__":
    def foo(n: int) -> int:
        return 35 // n
    assert suppress(partial(foo, 1), ())() == 35 == foo(1)
    suppress(partial(foo, 0), (ZeroDivisionError,))()
    # suppress(partial(foo, 0), ())()
