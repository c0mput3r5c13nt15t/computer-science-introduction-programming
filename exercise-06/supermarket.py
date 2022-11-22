from dataclasses import dataclass


@dataclass
class Food:
    expiration_date: str


@dataclass
class NonFood:
    pass


@dataclass
class Stock:
    name: str
    units: int
    price_per_unit: int
    kind: Food | NonFood


def is_expired(stock: Stock, date: str) -> bool:
    if isinstance(stock.kind, Food):
        return date > stock.kind.expiration_date
    else:
        return False


def get_expired(stocks: list[Stock], date: str) -> list[Stock]:
    return_stocks = []
    for stock in stocks:
        if is_expired(stock, date):
            return_stocks.append(stock)
    return return_stocks


def buy(stock: Stock, units: int) -> int:
    if units > stock.units:
        units = stock.units
    stock.units -= units
    return units
