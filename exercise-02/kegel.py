import math


def coneShellSurface(radius: float, height: float) -> float:
    return math.pi * radius * (radius**2 + height**2)**0.5


radius = float(input('Radius: '))
height = float(input('Höhe: '))
print('Matelfläche: %.2f' % coneShellSurface(radius, height))
