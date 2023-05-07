from typing import List


class Node:
    name: str
    children: List["Node"]

    def __init__(self, name, children):
        self.name = name
        self.children = children


def search(root, destination):

    distance = 0
    nodes = root.children

    if root.name == destination:
        # already there
        return distance

    while nodes:

        distance += 1

        for node in nodes:
            if node.name == destination:
                return distance

        nodes_new = []
        for node in nodes:
            nodes_new.extend(node.children)

        nodes = nodes_new

    return None


children_b = [Node("E", [])]
children_c = [Node("F", [])]
children_d = [Node("G", [Node("Last", [])])]
children = [Node("B", children_b), Node("C", children_c), Node("D", children_d)]
root = Node("A", children)


assert search(root, "A") == 0
assert search(root, "C") == 1
assert search(root, "E") == 2
assert search(root, "Last") == 3
assert search(root, "Nowheree") is None
