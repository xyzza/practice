import random
import pytest


def insertion_sort(array: list[int]) -> list[int]:
    # iteration through array
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array

@pytest.mark.parametrize("array", [
        [],
        [
            1,
        ],
        [1, 2],
        [2, 1],
        [
            6,
            5,
            4,
            3,
            1,
        ],
        [random.randint(1, 100) for _ in range(10)],
    ])
def test_insert_sort(array: list[int]) -> None:
    res = insertion_sort(array)
    assert res == sorted(array, reverse=True), (array, res)
