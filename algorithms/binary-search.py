"""
python 3.6
binary search algorithm implementation
"""


def binary_search(collection, value):

    left = 0
    right = len(collection) - 1

    while left <= right:

        middle = (left + right) // 2

        if collection[middle] == value:
            return middle

        if collection[middle] < value:
            # search right
            left = middle + 1

        if collection[middle] > value:
            # search left
            right = middle - 1

    return None


# tests:
assert binary_search([], 1) is None
assert binary_search([1, 3, 7, 9, 15, 17, 19, 23], 1) == 0
assert binary_search([1, 3, 7, 9, 15, 17, 19, 23], 23) == 7
assert binary_search([x for x in range(1, 11)], 1) == 0
assert binary_search([x for x in range(100)], 25) == 25
assert binary_search([-3, -1, 4, 7, 10, 21], -1) == 1
assert binary_search([-3, -1, 4, 7, 10, 21], -3) == 0
assert binary_search([-3, -1, 4, 7, 10, 21], 10) == 4
assert binary_search([-3, -1], -3) == 0
