from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List, Tuple
from collections import deque


@dataclass
class Node:
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def build_tree_level_order(values: List[Optional[int]]) -> Optional[Node]:
    """
    Builds a binary tree from a level-order representation (as in LeetCode):
    values[i] is either an int or None.
    """
    if not values or values[0] is None:
        return None

    root = Node(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            q.append(node.right)
        i += 1

    return root


def max_value_placeholder(root: Optional[Node]) -> Optional[int]:

    # base case
    if root is None:
        return None

    _max = root.val

    lval = max_value_placeholder(root.left)
    if lval is not None:
        _max = max(_max, lval)
    rval = max_value_placeholder(root.right)
    if rval is not None:
        _max = max(_max, rval)

    return _max


TEST_CASES: List[Tuple[List[Optional[int]], Optional[int]]] = [
    ([], None),  # 1) empty list -> empty tree
    ([None], None),  # 2) explicit empty tree
    ([1], 1),  # 3) single node
    ([1, 2, 3], 3),  # 4) simple case
    ([3, 9, 20, None, None, 15, 7], 20),  # 5) maximum is in the right subtree
    ([1, 2, None, 3, None, 4, None], 4),  # 6) left "linked list"
    ([1, None, 2, None, 3, None, 4], 4),  # 7) right "linked list"
    ([-10, -20, -3, None, -15], -3),  # 8) all negative values
    ([5, 5, 5, 5, None, None, 5], 5),  # 9) duplicates
    ([10, 5, 15, 3, 7, None, 18, None, 4], 18),  # 10) sparse tree
]


def main() -> None:
    for idx, (arr, expected) in enumerate(TEST_CASES, start=1):
        root = build_tree_level_order(arr)
        print(f"case #{idx}: input={arr}, expected_max={expected}")
        try:
            got = max_value_placeholder(root)
            print(f"  got={got} -> {'OK' if got == expected else 'FAIL'}")
        except NotImplementedError:
            print("  got=NotImplementedError (implement max_value_placeholder)")
        print()


if __name__ == "__main__":
    main()
