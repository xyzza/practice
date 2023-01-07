from typing import Optional, List, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    item: T
    parent: Optional["Node"]
    left: Optional["Node"]
    right: Optional["Node"]

    def __init__(
        self,
        item: T,
        parent: Optional["Node"],
        left: Optional["Node"],
        right: Optional["Node"],
    ) -> None:
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return str(f"Item: {self.item}")


def build_node(numbers: List[int], parent: Optional[Node[int]]):
    """numbers are sorted list of integers"""
    if not len(numbers):
        return None
    middle = len(numbers) // 2
    item = numbers[middle]
    node = Node(item=item, parent=parent, left=None, right=None)
    left = build_node(numbers[:middle], parent=node)
    right = build_node(numbers[middle + 1 :], parent=node)
    node.left = left
    node.right = right
    return node


def build_traversal(node: Node) -> List[int]:
    if node is None:
        return []
    return build_traversal(node.left) + [node.item] + build_traversal(node.right)


def find_depth(node: Node) -> int:
    """find length of path from node to root"""
    length = 0
    while node.parent:
        length += 1
        node = node.parent
    return length


def find_height(node: Node, height=0) -> int:
    if node is None:
        return height
    left_height = find_height(node.left, height=height+1)
    right_height = find_height(node.right, height=height+1)

    return max(left_height, right_height)


def find_root(node: Node) -> Node:
    return None


def find(root: Node, item: int) -> Optional[Node]:
    if root.item == item:
        return root
    left_search = find(root.left, item) if root.left else None
    right_search = find(root.right, item) if root.right else None
    if left_search:
        return left_search
    return right_search


def subtree_first(node: Node) -> Optional[Node]:
    if node.left is not None:
        return subtree_first(node.left)
    return node


def subtree_last(node: Node) -> Optional[Node]:
    if node.right is not None:
        return subtree_last(node.right)
    return node


def insert_item(root: Node, item: int) -> Node:
    return None


def delete_item(root: Node, item: int) -> Optional[int]:
    return -1


def next_node(item: int) -> Optional[Node]:
    return None


def prev_node(item: int) -> Optional[Node]:
    return None


def build_letter_tree() -> Node[str]:
    root = Node('A', None, None, None)
    b = Node('B', parent=root, left=None, right=None)
    c = Node('C', parent=root, left=None, right=None)
    root.left, root.right = b, c
    d = Node('D', parent=b, left=None, right=None)
    e = Node('E', parent=b, left=None, right=None)
    b.left, b.right = d, e
    f = Node('F', parent=d, left=None, right=None)
    d.left = f
    return root


if __name__ == "__main__":
    int_tree = build_node(numbers=[x for x in range(11)], parent=None)
    print(build_traversal(int_tree))
    letter_tree = build_letter_tree()
    print(build_traversal(letter_tree))
    node_2 = find(int_tree, 2)
    node_e = find(letter_tree, 'E')
    print(find_height(int_tree))
    print(find_height(letter_tree))
    print(find_height(node_2))
    print(find_height(node_e))
    print(subtree_first(int_tree))
    print(subtree_last(int_tree))
    print(subtree_first(letter_tree))
    print(subtree_last(letter_tree))
