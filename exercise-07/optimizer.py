from tree import Node, Var, Val, Op, OpSym
from parser import parse
from typing import Optional


def node_to_str(node: Node) -> str:
    match node:
        case Var(name):
            return name
        case Val(value):
            return str(value)
        case Op(sym, left, right):
            return f"({node_to_str(left)} {sym.value} {node_to_str(right)})"


def node_to_str_if(node: Node) -> str:
    if type(node) is Var:
        return node.name
    elif type(node) is Val:
        return str(node.value)
    elif type(node) is Op:
        return f"({node_to_str_if(node.left)} {node.sym.value} {node_to_str_if(node.right)})"
    else:
        return ''


def optimize_step(node: Node) -> Optional[Node]:
    match node:
        case Var(_):
            return None
        case Val(_):
            return None
        case Op(sym, Val(x), Val(y)):
            match sym:
                case OpSym.ADD:
                    return Val(x + y)
                case OpSym.MUL:
                    return Val(x * y)
        case Op(OpSym.ADD, x, y) if x == y:
            return Op(OpSym.MUL, Val(2), x)
        case Op(sym_one, x, Op(sym_two, y, z)) if sym_one == sym_two:
            return Op(sym_one, Op(sym_one, x, y), z)
        case Op(sym, left, right) if optimize_step(left) is not None:
            return Op(sym, optimize_step(left), right)  # type: ignore
        case Op(sym, left, right) if optimize_step(right) is not None:
            return Op(sym, left, optimize_step(right))  # type: ignore
        case _:
            return None


def optimize_step_if(node: Node):
    if type(node) is Var or type(Node) is Val:
        return None
    elif type(node) is Op:
        if type(node.left) is Val and type(node.right) is Val:
            if node.sym.value == '+':
                return Val(node.left.value + node.right.value)
            elif node.sym.value == '*':
                return Val(node.left.value * node.right.value)
        elif node.sym.value == '+' and node.left == node.right:
            return Op(OpSym.MUL, Val(2), node.left)
        elif type(node.right) == Op and node.sym == node.right.sym:  # type: ignore
            # type: ignore
            return Op(node.sym, Op(node.sym, node.left, node.right.left), node.right.right)
        else:
            optimize_left = optimize_step(node.left)
            if optimize_left is not None:
                return Op(node.sym, optimize_left, node.right)

            optimize_right = optimize_step(node.right)
            if optimize_right is not None:
                return Op(node.sym, node.left, optimize_right)

            return None


def optimize(node: Optional[Node]) -> list[Node]:
    if node is None:
        return []
    else:
        return [node] + optimize(optimize_step(node))


if __name__ == '__main__':
    e = Op(OpSym.ADD, Op(OpSym.MUL, Val(2), Var('x')), Val(5))
    assert node_to_str(e) == '((2 * x) + 5)'
    assert node_to_str(Var('x')) == 'x'
    assert node_to_str(Val(2)) == '2'

    assert node_to_str_if(e) == '((2 * x) + 5)'
    assert node_to_str_if(Var('x')) == 'x'
    assert node_to_str_if(Val(2)) == '2'

    assert optimize_step(Op(OpSym.ADD, Var('x'), Var('x'))
                         ) == Op(OpSym.MUL, Val(2), Var('x'))
    assert optimize_step(Op(OpSym.ADD, Var('x'), Var('y'))) is None
    e = Op(OpSym.MUL, Val(3), Var('x'))
    assert optimize_step(Op(OpSym.ADD, e, e)) == Op(OpSym.MUL, Val(2), e)

    e1 = Op(OpSym.MUL, Val(2), Val(3))
    e2 = Op(OpSym.MUL, Val(3), Val(2))
    assert optimize_step(Op(OpSym.ADD, e1, e2)) == Op(OpSym.ADD, Val(6), e2)
    assert optimize_step(Op(OpSym.ADD, Val(6), e2)) == Op(
        OpSym.ADD, Val(6), Val(6))
    assert optimize_step(Op(OpSym.ADD, Val(6), Val(6))) == Val(12)
    assert optimize_step(Val(12)) is None

    assert optimize_step_if(Op(OpSym.ADD, Var('x'), Var('x'))
                            ) == Op(OpSym.MUL, Val(2), Var('x'))
    assert optimize_step_if(Op(OpSym.ADD, Var('x'), Var('y'))) is None
    e = Op(OpSym.MUL, Val(3), Var('x'))
    assert optimize_step_if(Op(OpSym.ADD, e, e)) == Op(OpSym.MUL, Val(2), e)

    e1 = Op(OpSym.MUL, Val(2), Val(3))
    e2 = Op(OpSym.MUL, Val(3), Val(2))
    assert optimize_step_if(Op(OpSym.ADD, e1, e2)) == Op(OpSym.ADD, Val(6), e2)
    assert optimize_step_if(Op(OpSym.ADD, Val(6), e2)) == Op(
        OpSym.ADD, Val(6), Val(6))
    assert optimize_step_if(Op(OpSym.ADD, Val(6), Val(6))) == Val(12)
    assert optimize_step_if(Val(12)) is None

    assert optimize(parse('(x + x) + (x + x)')) == [
        parse('(x + x) + (x + x)'),
        parse('(2 * (x + x))'),
        parse('(2 * (2 * x))'),
        parse('((2 * 2) * x)'),
        parse('(4 * x)')
    ]

    user_input = input('> ')
    while user_input != 'quit':
        parsed = parse(user_input)
        if parsed:
            optimize_steps = optimize(parse(user_input))
            for step in optimize_steps:
                print(f"= {node_to_str(step)}")
        else:
            print('Syntax error.')
        user_input = input('\n> ')
    print('Good bye!')
