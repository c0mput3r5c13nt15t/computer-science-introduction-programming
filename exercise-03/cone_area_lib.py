from math import pi


def cone_area(radius: float, height: float) -> float:
    return round(pi * radius * (radius**2 + height**2)**0.5, 2)
