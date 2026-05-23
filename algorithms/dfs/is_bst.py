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

from math import inf

def is_valid_bst(root: Optional[Node]) -> bool:

    def dfs(node: Node | None, left: int, right: int) -> bool:
        if node is None:
            return True
        if not(left < node.val < right):
            return False

        return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        

    return dfs(root, -inf, inf)


TEST_CASES: List[Tuple[List[Optional[int]], bool]] = [
    ([], True),                                      # 1)  пустое дерево — BST
    ([None], True),                                  # 2)  явно пустое дерево — BST
    ([1], True),                                     # 3)  один узел — BST
    ([2, 1, 3], True),                               # 4)  классический минимальный BST
    ([5, 1, 4, None, None, 3, 6], False),            # 5)  правый ребёнок (4) меньше корня (5)
    ([10, 5, 15, None, None, 6, 20], False),         # 6)  6 в правом поддереве меньше корня
    ([5, 4, 6, None, None, 3, 7], False),            # 7)  нарушение на глубине 2 (3 < 5)
    ([3, 1, 5, None, 2, 4, 6], True),                # 8)  корректный BST глубиной 3
    ([2, 2, 2], False),                              # 9)  дубликаты — не BST (строгое неравенство)
    ([1, None, 2, None, 3, None, 4], True),          # 10) правый «связный список» — BST
    ([4, 3, None, 2, None, 1], True),                # 11) левый «связный список» — BST
    ([10, 5, 15, 3, 7, 12, 20], True),               # 12) полный сбалансированный BST
    ([10, 5, 15, 3, 7, 12, 20, None, None, 6, 8],   True),  # 13) глубже с корректными границами
    ([-5, -10, -3, None, None, -7, -1], False),      # 13) отрицательные значения, нарушение (-7 < -5 в правом)
    ([-10, -20, -5, None, None, -7, -3], True),      # 14) корректный BST с отрицательными значениями
]


def main() -> None:
    for idx, (arr, expected) in enumerate(TEST_CASES, start=1):
        root = build_tree_level_order(arr)
        print(f"case #{idx}: input={arr}, expected_is_bst={expected}")
        try:
            got = is_valid_bst(root)
            print(f"  got={got} -> {'OK' if got == expected else 'FAIL'}")
        except NotImplementedError:
            print("  got=NotImplementedError (implement is_valid_bst)")
        print()


if __name__ == "__main__":
    main()