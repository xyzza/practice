"""
Created a binary tree in traversal order
Each node is a dictionary with the following keys:
    parent: the parent node
    left: the left child node
    right: the right child node
    value: the value of the node
"""
from typing import Optional, Union
from .model import Node


# def build_node(
#     parent: Optional[dict],
#     value: Union[int, str],
#     left: Optional[dict],
#     right: Optional[dict],
# ) -> Node:
#     return


def build_balanced(
    initial_input: list[int | str], parent: Node | None
) -> Optional[Node]:

    if len(initial_input) == 0:
        return None

    mid_index = len(initial_input) // 2
    node = Node(
        value=initial_input[mid_index], left=None, right=None, parent=parent
    )

    left_node = build_balanced(initial_input[:mid_index], node)
    right_node = build_balanced(initial_input[mid_index + 1 :], node)
    node.left = left_node if left_node else None
    node.right = right_node if right_node else None
    return node
