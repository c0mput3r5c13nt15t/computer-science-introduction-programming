# Aufgabe 4 (Dataclasses) #####################################################

from dataclasses import dataclass


# (a) #########################################################################

@dataclass
class Name:
    prename: str
    surname: str

    def __lt__(self, other: 'Name'):
        return self.surname < other.surname


# (b) #########################################################################

@dataclass
class Event:
    event: tuple[int, int] | str


def log_event(event: Event):
    match event.event:
        case (x, y):
            print(f"Mouse clicked at ({x}, {y}).")
        case str(x):
            print(f"Key '{x}' pressed.")

# (c) #########################################################################


@dataclass
class GameObject:
    x: int
    y: int

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy


@dataclass
class Player(GameObject):
    health: int

    def __post_init__(self):
        assert self.health >= 0


if __name__ == "__main__":
    n1 = Name('Paul', 'Maier')
    n2 = Name('Daniel', 'Meiborg')

    assert n1 < n2

    # e = Event((3, 2))
    # log_event(e)

    # e2 = Event('a')
    # log_event(e2)

    p = Player(1, 2, 100)
    p.move(-1, -2)
    assert p.x == 0 and p.y == 0 and p.health == 100

    # p2 = Player(1, 2, -3) ⇾ Throws an error
