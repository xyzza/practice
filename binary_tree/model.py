from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return (
            f"VAL:{self.value} "
            f"left:{self.left.value if self.left else None} "
            f"right:{self.right.value if self.right else None} "
            f"parent:{self.parent.value if self.parent else None}"
        )
