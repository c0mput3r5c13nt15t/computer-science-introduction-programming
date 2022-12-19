from dataclasses import dataclass
from typing import Union


def apply_binary_operator(op: str, a: float, b: float) -> float:
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case _:
            raise ValueError(f"Unknown operator {op}")


@dataclass
class Vector():
    __values: list[float]

    def __post_init__(self):
        assert len(self.values) > 0, "Dimension must be greater than 0"

        self.__dimension = len(self.values)
        self.__len = sum([x**2 for x in self.values])**0.5

    @property
    def values(self) -> list[float]:
        return self.__values

    @property
    def dimension(self) -> int:
        return self.__dimension

    @property
    def len(self) -> float:
        return self.__len

    def __str__(self) -> str:
        return f"{self.dimension}D vector: {self.values}"

    def __pos__(self) -> 'Vector':
        return Vector(self.values)

    def __neg__(self) -> 'Vector':
        negated_values = []
        for value in self.values:
            negated_values.append(-value)
        return Vector(negated_values)

    def operate_binary(self, op: str, other: Union['Vector', int, float]) -> 'Vector':
        match other:
            case Vector(values):
                if self.dimension != other.dimension:
                    raise ValueError("Vectors must have the same dimension")

                new_values = []
                for a, b in zip(self.values, values):
                    new_values.append(apply_binary_operator(op, a, b))

                return Vector(new_values)
            case int(b) | float(b):
                new_values = []
                for a in self.values:
                    new_values.append(apply_binary_operator(op, a, b))

                return Vector(new_values)
            case _:
                raise TypeError(f"Cannot operate with type {type(other)}")

    def __add__(self, other: Union['Vector', int, float]) -> 'Vector':
        return self.operate_binary("+", other)

    def __sub__(self, other: Union['Vector', int, float]) -> 'Vector':
        return self.operate_binary("-", other)

    def __mul__(self, other: Union['Vector', int, float]) -> 'Vector':
        return self.operate_binary("*", other)

    def __radd__(self, other: Union['Vector', int, float]) -> 'Vector':
        return self.operate_binary("+", other)

    def __rsub__(self, other: Union['Vector', int, float]) -> 'Vector':
        return -self.operate_binary("-", other)

    def __rmul__(self, other: Union['Vector', int, float]) -> 'Vector':
        return self.operate_binary("*", other)
