# Aufgabe 8 (Funktionale Programmierung) ######################################


# (a) #########################################################################

def times_2(f):
    return lambda x: f(x) * 2


# (b) #########################################################################

def map_matrix(f, m):
    return [[f(a) for a in b] for b in m]


# (c) #########################################################################

def map_matrix_2(f, m):
    return list(map(lambda x: list(map(f, x)), m))


if __name__ == "__main__":
    def f(x): return x + 1
    g = times_2(f)
    assert g(3) == 8

    example = [[1, 2, 3], [4, 5, 6]]
    assert map_matrix(lambda x: x * 2, example) == [[2, 4, 6], [8, 10, 12]]
    assert map_matrix_2(lambda x: x * 2, example) == [[2, 4, 6], [8, 10, 12]]
