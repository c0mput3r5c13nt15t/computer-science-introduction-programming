# Aufgabe 7 (Generators) ######################################################


# (a) #########################################################################

def my_chain(xs, ys):
    for x in xs:
        yield x
    for y in ys:
        yield y


# (b) #########################################################################

def dup(n, xs):
    for x in xs:
        for i in range(n):
            yield x


# (c) #########################################################################

def compare(xs, ys):
    for i in range(min(len(xs), len(ys))):
        if xs[i] < ys[i]:
            yield ys[i]
        else:
            yield xs[i]


if __name__ == "__main__":
    assert list(my_chain(range(5), range(2))) == [0, 1, 2, 3, 4, 0, 1]
    assert list(dup(3, range(1, 4))) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert list(compare(range(6), range(-3, 7, 3))) == [0, 1, 3, 6]
