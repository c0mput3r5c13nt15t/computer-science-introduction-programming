from typing import Iterator

# Generator !


def lines(path: str) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            yield line.strip()


def parse_csv(lines: Iterator[str]) -> Iterator[list[str]]:
    while True:
        try:
            next_line = next(lines)
            yield next_line.split(',')
        except StopIteration:
            return


def update_balance(balance: float, csv_path: str) -> float:
    costs = list(parse_csv(lines(csv_path)))[1:]
    return balance + sum(list(map(lambda x: float(x[2]), costs)))


if __name__ == "__main__":
    for line in lines("exercise-13/umsatz.csv"):
        print(line)

    assert update_balance(100.00, "exercise-13/umsatz.csv") == 170.8
