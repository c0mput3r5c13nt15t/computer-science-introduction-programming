from progress.bar import Bar
import time


class Item:
    def __init__(self, name: str, description: str, value: int) -> None:
        self.name = name
        self.description = description
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class Room:
    def __init__(self, name: str, description: str, items: list[Item]) -> None:
        self.name = name
        self.description = description
        self.items = items


class Spacecraft:
    def __init__(self, name: str, layout: list[tuple[Room, Room]]) -> None:
        self.name = name
        self.layout = layout

    def __str__(self) -> str:
        return self.name

    def printFloorplan(self) -> None:
        print(f"Floorplan of {self.name}")
        for room1, room2 in self.layout:
            print(f"{room1.name} <-> {room2.name}")


class Character:
    def __init__(self, name: str, location: Room, inventory: list[Item] = []) -> None:
        self.name = name
        self.location = location
        self.inventory = inventory

    def printInventory(self) -> None:
        print(f"{self.name}'s inventory:")
        for item in self.inventory:
            print(str(item))

    def addItem(self, item: Item) -> None:
        self.inventory.append(item)

    def removeItem(self, item: Item) -> None:
        self.inventory.remove(item)


class Player(Character):
    def __init__(self, name: str, location: Room, inventory: list[Item] = []) -> None:
        super().__init__(name, location, inventory)


class NPC(Character):
    def __init__(self, name: str, location: Room, inventory: list[Item] = []) -> None:
        super().__init__(name, location, inventory)


def makeStringSpecificLength(string: str, length: int, fill: str = ' ') -> str:
    return string + fill * (length - len(string))


def typingAnimation(text: str, speed: float = 0.1) -> None:
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed)
    # End formatting
    print('')


def dialogue(npc: NPC, text: str) -> None:
    typingAnimation(f"{npc.name}: {text}")


def progessBar(title: str, fill: str = '#', speed: float = 0.1) -> None:
    bar = Bar(title, max=20, fill=fill, suffix='%(percent)d%%', )
    for i in range(20):
        time.sleep(speed)
        bar.next()
    bar.finish()


def prompt(question: str, options: list[str] | None = None) -> str | int:
    print('')
    typingAnimation(question)
    if options is not None:
        for i in range(len(options)):
            print(f"[{i}] {options[i]}")
        while True:
            try:
                choice = int(input(">>> "))
                if choice in range(len(options)):
                    return choice
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid choice")
    else:
        returnInput = input(">>> ")
        print('')
        return returnInput
