from math import pi


def coneShellSurface(radius: float, height: float) -> float:
    return pi * radius * (radius**2 + height**2)**0.5


if __name__ == '__main__':
    radius = float(input('Radius: '))
    height = float(input('Höhe: '))
    print('Matelfläche: %.2f' % coneShellSurface(radius, height))
