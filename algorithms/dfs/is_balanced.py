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


def is_balanced_placeholder(root: Optional[Node]) -> bool:

    def dfs(node: Node) -> int:

        if node is None:
            return 0

        l = dfs(node.left)
        if l == -1:
            return l
        r = dfs(node.right)
        if r == -1:
            return r

        if abs(l-r) > 1:
            return -1

        return max(l, r) + 1

    return dfs(root) !=

TEST_CASES: List[Tuple[List[Optional[int]], bool]] = [
    ([], True),  # 1) empty list -> empty tree (balanced)
    ([None], True),  # 2) explicit empty tree (balanced)
    ([1], True),  # 3) single node (balanced)
    ([1, 2, 3], True),  # 4) two children (balanced)
    ([3, 9, 20, None, None, 15, 7], True),  # 5) classic balanced example
    ([1, 2, 2, 3, 3, None, None, 4, 4], False),  # 6) classic unbalanced example
    ([1, 2, None, 3, None, 4, None], False),  # 7) left "linked list" (unbalanced)
    ([1, None, 2, None, 3, None, 4], False),  # 8) right "linked list" (unbalanced)
    ([1, 2, 3, 4, 5, None, None], True),  # 9) slightly deeper left side but still balanced
    ([1, 2, 3, 4, None, None, None, 5], False),  # 10) imbalance occurs below the root
    ([-10, -20, -3, None, -15], True),  # 11) includes negatives (still balanced)
    ([5, 5, 5, 5, None, None, 5], True),  # 12) duplicates (balanced)
]


def main() -> None:
    for idx, (arr, expected) in enumerate(TEST_CASES, start=1):
        root = build_tree_level_order(arr)
        print(f"case #{idx}: input={arr}, expected_balanced={expected}")
        try:
            got = is_balanced_placeholder(root)
            print(f"  got={got} -> {'OK' if got == expected else 'FAIL'}")
        except NotImplementedError:
            print("  got=NotImplementedError (implement is_balanced_placeholder)")
        print()


if __name__ == "__main__":
    main()