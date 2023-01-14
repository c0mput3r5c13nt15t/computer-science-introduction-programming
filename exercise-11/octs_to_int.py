from functools import reduce


def octs_to_int(digits: list[int]) -> int:
    return reduce(lambda x, y: x * 8 + y, digits)


if __name__ == "__main__":
    print(octs_to_int([6, 4, 4]))
    assert octs_to_int([6, 4, 4]) == 420
