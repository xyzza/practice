"""
Find min length of a subsequnce, that consists of 0,1,2
from unordered sequence of numbers {0,1,2}
If no subsequnce - return -1
"""


INPUTS = [("000010200002", 3), ("00010001", -1), ("1000002", 7)]


def main(string: str) -> int:
    indexes = [-1, -1, -1]
    min_len = len(string) + 1

    for i, num in enumerate(string):
        num = int(num)
        indexes[num] = i

        if len([i for i in indexes if i > -1]) == 3:
            new_len = max(indexes) - min(indexes)
            if new_len < min_len:
                min_len = new_len + 1

    return min_len if min_len < len(string) + 1 else -1


if __name__ == "__main__":
    for (inpt, expct) in INPUTS:
        assert main(inpt) == expct
