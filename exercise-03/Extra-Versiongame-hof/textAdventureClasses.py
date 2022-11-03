from random import choice


class Item:
    def __init__(self, name: str, description: str, value: int) -> None:
        self.name = name
        self.description = description
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class Spacecraft:
    def __init__(self, name: str, graphic: str, crew: int, cargoSpace: int, speed: int, damage: int, hull: int, shields: int) -> None:
        self.name = name
        self.graphic = graphic
        self.crew = crew
        self.cargoSpace = cargoSpace
        self.speed = speed
        self.damage = damage
        self.hull = hull
        self.shields = shields

    def __str__(self) -> str:
        return f"{self.graphic}\n{self.name} - Crew: {self.crew} - Cargo Space: {self.cargoSpace} - Speed: {self.speed} - Damage: {self.damage} - Hull: {self.hull} - Shields: {self.shields}"


Aqua = Spacecraft("Aqua", """
   :::-
    ] [] [=] [-*@
   [  []}{
    ] [] [=] [-*@
   :::-
""", 10, 10, 18, 19, 81, 50)
Copbra = Spacecraft("Cobra", """
   }{=
     D-) (0()8<)]X(
   +[] X=0} {|X()*<>**
     D-) (0()8<)]X(
   }{=
""", 34, 35, 131, 141, 132, 3)
Stinger = Spacecraft("Stinger", """
    888))=
    -)-)-))-))-))-))-))
   (X==<>==X)>
    -)-)-))-))-))-))-))
    888))=
""", 20, 5, 40, 260, 102, 28)
Spike = Spacecraft("Spike", """
   8-8)=
   ) ((@)[
   -<  *) (> <] [
   ) ((@)[
   8-8)=
""", 12, 2, 13, 380, 88, 0)
Nimbus = Spacecraft("Nimbus", """
   ---x---
     -)8-8(=
   {}(&)
     -)8-8(=
     -x-
""", 8, 5, 34, 39, 76, 0)
Tsar = Spacecraft("Tsar", """
    88((=
   -)-)-)-)-)-)
   [~] (x-x-x)><(x-x-x)
   -)-)-)-)-)-)
    88((=
""", 43, 30, 5, 90, 337, 20)
Shockwave = Spacecraft("Shockwave", """
    88((+
   8-8((+
   -][  O] [<)] [O(!)
   8-8((+
    88((+
""", 17, 20, 42, 93, 69, 0)
Vortex = Spacecraft("Vortex", """
   <---x x--->
    {}8<>[=<><><() (D8
   +[]  X|)}8|] [8()) ((-
    {}8<>[=<><><() (D8
     <-x x->
""", 40, 33, 54, 58, 427, 0)
Phazek = Spacecraft("Phazek", """
   8-8((=
     =+))|o|((+=
   :x:  (X==<>==X)>
     =+))|o|((+=
   8-8((=
""", 13, 80, 73, 110, 315, 0)
Tilde = Spacecraft("Tilde", """
   \\~\\
    ){<>] [> <:=>
   {@(!)<>-:=}-) (8()
    ){<>] [> <:=>
   /~/
""", 11, 5, 78, 34, 112, 50)
Pling = Spacecraft("Pling", """
   \\.
     (+)===\
   O=|-|OOOOO
     (+)===/
   /.
""", 30, 300, 19, 20, 100, 67)
Stray = Spacecraft("Stray", """
     \\+\\
    ]D-)@=<>) (]()<>
   (=+(-)+=)
    ]D-)@=<>) (]()<>
     /+/
""", 25, 15, 50, 76, 189, 16)

# class Character:
#     def __init__(self, name: str, inventory: list[Item] = []) -> None:
#         self.name = name
#         self.inventory = inventory

#     def printInventory(self) -> None:
#         print(f"{self.name}'s inventory:")
#         for item in self.inventory:
#             print(str(item))

#     def addItem(self, item: Item) -> None:
#         self.inventory.append(item)

#     def removeItem(self, item: Item) -> None:
#         self.inventory.remove(item)


# class Player(Character):
#     def __init__(self, name: str, inventory: list[Item] = []) -> None:
#         super().__init__(name, inventory)
#         self.username = ""
#         self.password = ""


class Game:
    def __init__(self) -> None:
        self.username: str = ""
        self.password: str = ""
        self.playerSpaceship: Spacecraft = Stray
        self.distressSignalSent: bool = False
        self.enemySpaceships: list[Spacecraft] = []

    def newEnemySpaceship(self) -> None:
        self.enemySpaceships.append(choice(
            [Aqua, Copbra, Stinger, Spike, Nimbus, Tsar, Shockwave, Vortex, Phazek, Tilde, Pling]))

    def reset(self) -> None:
        self.username = ""
        self.password = ""
        self.playerSpaceship = Stray
        self.distressSignalSent = False
        self.enemySpaceships = []
