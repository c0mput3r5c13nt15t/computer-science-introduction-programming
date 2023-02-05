# Aufgabe 3 (Strings) #########################################################

def is_list_of_int(x: str) -> bool:
    print("x", x)
    if not x.startswith('[') or not x.endswith(']'):
        return False

    for char in x:
        if char not in '1234567890-,[]':
            return False

    numbers = x[1:-1].split(',')

    if len(numbers) == 0 or len(numbers) <= x.count(',') or '' in numbers:
        return False

    for number in numbers:
        try:
            int(number)
        except Exception:
            return False

    return True


if __name__ == "__main__":
    assert not is_list_of_int("100,-44,0")
    assert not is_list_of_int("100,-44,0]")
    assert not is_list_of_int("[100,-44,0")
    assert not is_list_of_int("[100,--44,0]")
    assert not is_list_of_int("[100,---44,0]")
    assert not is_list_of_int("[a,0]")
    assert not is_list_of_int("[-a,0]")
    assert not is_list_of_int("[1, 0]")
    assert not is_list_of_int("[1,,0]")
    assert not is_list_of_int("[]")
    assert not is_list_of_int("[123,456,]")

    assert is_list_of_int("[-44]")
    assert is_list_of_int("[44]")
    assert is_list_of_int("[100,-44,0]")
