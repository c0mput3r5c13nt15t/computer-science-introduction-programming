import functools
import time


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fast_and_simple(n - 1) + fib_fast_and_simple(n - 2)


def fib_fast(n: int) -> int:
    return fib_fast_cache(n, dict())


def fib_fast_cache(n: int, cache: dict[int, int]) -> int:
    # If we already computed fib(n), then return the previously computed result.
    if n in cache:
        return cache[n]
    # Otherwise we compute the result,
    result = None
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib_fast_cache(n - 1, cache) + fib_fast_cache(n - 2, cache)
    # put the result in the cache - in case we need it again later,
    cache[n] = result
    # and return the result.
    return result


def cached(f, cache: dict = dict()):
    @functools.wraps(f)
    def wrapper(*args):
        # Only works for one argument and no keyword arguments.
        arg_0 = args[0]
        if arg_0 in cache:
            return cache[arg_0]
        else:
            res = f(args[0])
            cache[arg_0] = res
            return res
    return wrapper


@cached
def fib_fast_and_simple(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fast_and_simple(n - 1) + fib_fast_and_simple(n - 2)


def time_function(f, n):
    print("Time the execution of %s(%s):" % (f.__name__, n), end=" ")
    t0 = time.time()
    f(n)
    delta = time.time() - t0
    print("%s sec." % delta)


if __name__ == "__main__":
    n = 200

    time_function(fib, n)
    time_function(fib_fast, n)
    time_function(fib_fast_and_simple, n)
