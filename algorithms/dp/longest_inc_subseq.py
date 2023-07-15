TEST = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
]


def main(nums: list[int]) -> int:

    n = len(nums)

    def dp(i, j):

        if i == n:
            res = 0
        else:
            res = dp(i + 1, j)
            if j == -1 or nums[i] > nums[j]:
                res = max(res, 1 + dp(i + 1, i))

        return res

    return dp(0, -1)


if __name__ == "__main__":
    for test, expected in TEST:
        result = main(test)
        print(f"Sequence {test} have a longest subseq len:{result}")
        assert result == expected, (result, expected)
