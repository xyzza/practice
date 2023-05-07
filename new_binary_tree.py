from binary_tree.build_tree import build_balanced
from binary_tree.model import Node

A = Node(value="A")
B = Node(value="B", parent=A)
C = Node(value="C", parent=A)
D = Node(value="D", parent=B)
E = Node(value="E", parent=B)
F = Node(value="F", parent=D)

A.left = B
A.right = C
B.left = D
B.right = E
D.left = F
print(B)


# def traversal(root: Node):
#     left = root.left
#     right = root.right
#     l_nodes = traversal(left) if left else []
#     r_nodes = traversal(right) if right else []
#     return (
#         l_nodes
#         + [
#             root.value,
#         ]
#         + r_nodes
#     )


# def traversal(root: Node):
#     """preorder traversal"""
#     res = []
#
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node is None:
#             continue
#         res.append(node.value)
#         stack.append(node.right)
#         stack.append(node.left)
#     return res


def traversal(root: Node):
    """inorder traversal"""
    res = []

    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.value)
        print(node)
        node = node.right
    return res


# def traversal(root: Node):
#     """postorder traversal"""
#     res = []
#
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node is None:
#             continue
#         res.append(node.value)
#         stack.append(node.left)
#         stack.append(node.right)
#     return res[::-1]


def get_first(node: Node) -> Node:
    if node.left is None:
        return node
    while node.left is not None:
        node = node.left
    return node


def get_last(node: Node) -> Node:
    if node.right is None:
        return node
    while node.right is not None:
        node = node.right
    return node


def get_successor(node: Node) -> Node:
    if node.right is not None:
        return get_first(node.right)
    while node.parent is not None and node.parent.right == node:
        node = node.parent
    return node.parent


def get_predecessor(node: Node) -> Node:
    if node.left is not None:
        return get_last(node.left)
    while node.parent is not None and node.parent.left == node:
        node = node.parent
    return node.parent


def delete(node: Node) -> None:
    if node.left is None and node.right is None:
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
    elif node.left:
        predecessor = get_predecessor(node)
        node.value = predecessor.value
        delete(predecessor)
    else:
        successor = get_successor(node)
        node.value = successor.value
        delete(successor)


if __name__ == "__main__":
    root = build_balanced([x for x in range(15)], None)
    print(traversal(root))
    print("FIRST:", get_first(root))
    print("LAST:", get_last(root))
    print("SUCCESSOR:", get_successor(root))
    print("PREDECESSOR:", get_predecessor(root))

    print(traversal(A))
    print("FIRST:", get_first(A))
    print("LAST:", get_last(A))
    print("SUCCESSOR:", get_successor(A))
    print("PREDECESSOR:", get_predecessor(A))
