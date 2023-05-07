"""
Definition of a problem:

Input: Linked list L with names
program should reverse second half of linked List
Additional memory complexity shouldn't be involved
Input: (Ron)->(Smith)->(Sara)->(Ellison)->(Jamie)->(Alex)
Output: (Ron)->(Smith)->(Sara)->(Alex)->(Jamie)->(Ellison)

NUmber of inputs always even
"""

INPUT_DATA = ["Ron", "Smith", "Sara", "Ellison", "Jamie", "Alex"]
EXPECTED_OUTPUT = ["Ron", "Smith", "Sara", "Alex", "Jamie", "Ellison"]


class LinkedList:
    def __init__(self):
        self._head = None
        self._last = None
        self._length = 0

    def add_first(self, name):
        if self._head is None:
            self._head = [name, None]
            self._last = self._head
        else:
            self._head = [name, self._head]
        self._length += 1

    def add_last(self, name):
        node = [name, None]
        if self._last is None:
            self._last = node
            self._head = node
        else:
            self._last[1] = node
            self._last = node
        self._length += 1

    def __len__(self):
        return self._length

    def __iter__(self):
        self._current_node = self._head
        return self

    def __next__(self):
        while self._current_node:
            current = self._current_node
            self._current_node = self._current_node[1]
            return current
        raise StopIteration


# [1,->], [2,->], [3,->], [4,->]


def reverse_linked_list(linked_list):
    iter(linked_list)
    N = len(linked_list)
    middle = N // 2
    for _ in range(middle):
        a_node = next(linked_list)

    prev_node = None
    next_node = None
    for _ in range(N - middle):
        node = next(linked_list) if next_node is None else next_node
        next_node = node[1]
        node[1] = prev_node
        prev_node = node

    a_node[1] = prev_node


def main():
    # initialize the linked list
    linked_list = LinkedList()
    for name in INPUT_DATA:
        linked_list.add_last(name)
    # check if linked list is correct
    result = [node[0] for node in linked_list]
    print(result)
    assert result == INPUT_DATA
    reverse_linked_list(linked_list)
    result = [node[0] for node in linked_list]
    print(result)
    assert result == EXPECTED_OUTPUT


if __name__ == "__main__":
    main()
