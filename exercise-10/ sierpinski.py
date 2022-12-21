from turtle import pendown, penup, setup, hideturtle, speed, forward, left, right

# 0L-System
# V = {F, G, +, -}
# w = F-G-G
# P = {F -> F-G+F+G-F, G -> GG}


def zeroLSystem(w: str, P: dict[str, str], n: int) -> str:
    for i in range(n):
        w = ''.join([P[c] if c in P else c for c in w])
    return w


def turtle_setup():
    setup(600, 600)
    speed(0)
    hideturtle()
    pendown()


def sierpinski(size: int, n: int):
    V = ['F', 'G', '+', '-']
    w = 'F-G-G'
    P = {'F': 'F-G+F+G-F', 'G': 'GG'}
    sierpinski = zeroLSystem(w, P, n)

    turtle_setup()
    for c in sierpinski:
        if c == 'F' or c == 'G':
            forward(size)
        elif c == '+':
            left(120)
        elif c == '-':
            right(120)


if __name__ == '__main__':
    # V = ['F', 'G', '+', '-']
    w = 'F-G-G'
    P = {'F': 'F-G+F+G-F', 'G': 'GG'}
    print(zeroLSystem(w, P, 2))
    sierpinski(33, 3)
