# Aufgabe 5 (Tests) ###########################################################

def is_strong(pw: str) -> bool:
    int_count = 0
    upper_count = 0
    used_specials = []

    for c in pw:
        if c.isupper():
            upper_count += 1
        elif c.isdigit():
            int_count += 1
        elif not c.islower():
            used_specials += [c]

    if int_count < 1:
        return False
    elif int_count <= 3:
        if len(used_specials) > 0:
            used_specials.pop(0)
        else:
            return False

    if upper_count <= 2:
        if len(used_specials) > 0:
            used_specials.pop(0)
        else:
            return False
    return True


def test_int_count_smaller_1():
    assert not is_strong('')
    assert not is_strong('abc')


def test_int_count_smaller_4():
    assert not is_strong('1')
    assert not is_strong('12')
    assert not is_strong('123')


def test_upper_count():
    assert not is_strong('1234')
    assert not is_strong('1234A')
    assert not is_strong('1234AA')

    assert not is_strong('123!')
    assert not is_strong('123!A')
    assert not is_strong('123!AA')


def test_strong_password():
    assert is_strong('1234AAA')
    assert is_strong('123!AAA')
    assert is_strong('1234AA!')
    assert is_strong('123!AA!')
