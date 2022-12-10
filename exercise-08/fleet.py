from dataclasses import dataclass


@dataclass
class Fahrzeug:
    zustand: int
    neupreis: int
    leergewicht: int
    baujahr: int

    def gewicht(self: 'Fahrzeug') -> int:
        return self.leergewicht

    def maut(self: 'Fahrzeug') -> int:
        raise NotImplementedError

    def alter(self: 'Fahrzeug') -> int:
        return max(2022 - self.baujahr - 1, 0)

    def marktwert(self: 'Fahrzeug') -> int:
        prozentwert = self.zustand - 5 * self.alter()
        # Annahme, dass nach int gefragt ist, da das Beispiel auf dem Lösungsblatt dies suggeriert
        return max(int(prozentwert / 100 * self.neupreis), 0)

    def __post_init__(self: 'Fahrzeug'):
        assert 0 <= self.zustand <= 100, f"Zustand {self.zustand}% muss zwischen 0% und 100% liegen."
        assert self.neupreis >= 0, f"Neupreis {self.neupreis}€ muss mindestens 0€ sein."
        assert self.leergewicht > 0, f"Leergewicht {self.leergewicht}kg muss größer als 0kg sein."
        assert self.baujahr > 1990, f"Baujahr {self.baujahr} muss größer als 1900 sein."


@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung: int
    sitzplaetze: int

    def gewicht(self: 'Kraftfahrzeug') -> int:
        return super().gewicht()

    def plaetze(self: 'Kraftfahrzeug') -> int:
        return self.sitzplaetze

    def maut(self: 'Kraftfahrzeug') -> int:
        return int(self.gewicht() / 5 + 25 * self.plaetze())

    def __post_init__(self: 'Kraftfahrzeug'):
        super().__post_init__()
        assert self.leistung > 0, f"Leistung {self.leistung}kW muss größer als 0kW sein."
        assert self.sitzplaetze > 0, f"Sitzplätze {self.sitzplaetze} muss größer als 0 sein."


@dataclass
class Bus(Kraftfahrzeug):
    stehplaetze: int

    def plaetze(self: 'Bus') -> int:
        return super().plaetze() + self.stehplaetze

    def __post_init__(self: 'Bus'):
        super().__post_init__()
        assert self.stehplaetze <= self.sitzplaetze, f"Stehplätze {self.stehplaetze} muss kleiner oder gleich Sitzplätze {self.sitzplaetze} sein."


@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def maut(self: 'Fahrzeug') -> int:
        return 0

    def marktwert(self: 'Fahrzeug') -> float:
        return super().marktwert() * 0.5

    def __post_init__(self: 'Fahrrad'):
        super().__post_init__()
        assert self.rahmengroesse > 0, f"Rahmengröße {self.rahmengroesse}cm muss größer als 0cm sein."


@dataclass
class PKW(Kraftfahrzeug):
    def __post_init__(self: 'PKW'):
        return super().__post_init__()


@dataclass
class LKW(Kraftfahrzeug):
    zuladung: int

    def gewicht(self: 'LKW'):
        return super().gewicht() + self.zuladung

    def __post_init__(self: 'LKW'):
        super().__post_init__()
        assert 0 < self.zuladung <= 2 * \
            self.leergewicht, f"Zuladung {self.zuladung}kg muss größer als 0kg und maximal {2 * self.leergewicht}kg sein."
