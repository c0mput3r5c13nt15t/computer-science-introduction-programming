from math import floor


def square(x: float) -> float:
    return x**2


def round_down_method_1(x: float) -> float:
    return float(floor(x))


def round_down_method_2(x: float) -> float:
    return float(int(x))


def round_down_method_3(x: float) -> float:
    return 10 * x // 10


if __name__ == '__main__':
    number = square(float(input('Kommazahl: ')))
    print('Quadriert:', number)
    print('Methode 1: %.1f' % round_down_method_1(number))
    print('Methode 2: %.1f' % round_down_method_2(number))
    print('Methode 3: %.1f' % round_down_method_3(number))
