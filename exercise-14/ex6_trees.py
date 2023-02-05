# Aufgabe 6 (Rekursion) #######################################################

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']


Tree = Optional[Node]


# (a) #########################################################################

def mark_at_path(tree: Node, path: str) -> str | None:
    current_node = tree

    if not path:
        return current_node.mark
    elif path[0] == 'l' and current_node.left:
        return mark_at_path(current_node.left, path[1:])
    elif path[0] == 'r' and current_node.right:
        return mark_at_path(current_node.right, path[1:])
    else:
        return None

# (b) #########################################################################


def paths(tree: Node | None) -> list[str]:
    if not tree:
        return []
    paths_left = []
    for path in paths(tree.left):
        paths_left += ["l" + path]
    paths_right = []
    for path in paths(tree.right):
        paths_right += ["r" + path]
    return [""] + paths_left + paths_right


if __name__ == "__main__":
    example = Node("n0",
                   Node("n1", None, None),
                   Node("n2",
                        Node("n3", None, None),
                        Node("n4", None, None)
                        )
                   )

    assert mark_at_path(example, "") == "n0"
    assert mark_at_path(example, "rl") == "n3"
    assert mark_at_path(example, "ll") is None

    assert paths(example) == ["", "l", "r", "rl", "rr"]
