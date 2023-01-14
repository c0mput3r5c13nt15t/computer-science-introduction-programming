def my_filter(xs: set, ys: set) -> set:
    return set(filter(lambda x: x not in ys, xs))


def my_diff(xs: set, ys: set) -> set:
    return set(filter(lambda z: not (z in xs and z in ys), xs.union(ys)))


if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    assert my_filter(set1, set2) == {1, 2}

    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    assert my_diff(set1, set2) == {1, 4}
