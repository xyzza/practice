from collections import Counter

TESTS = [
    ([3, 4, 2], 6),
    ([2, 2, 3, 3, 3, 4], 9),
    ([2, 4, 8, 10], 24),
    ([1], 1),
    ([1, 2], 2),
    ([1, 3], 4),
    ([1, 1, 1, 2, 4, 5, 5, 5, 6], 18),
    ([1, 1, 1], 3),
]


# T.O(m + n) M.O(n + k)
def del_earn(nums: list[int]) -> int:

    points = Counter(nums)

    for k, v in points.items():
        points[k] = k * v

    max_num = nums[0]
    for n in nums:
        max_num = max(max_num, n)

    def dp(num: int) -> int:

        if num in visited:
            return visited[num]

        if num < 1:
            res = 0
        else:
            res = max(points.get(num, 0) + dp(num - 2), dp(num - 1))
        visited[num] = res
        return res

    visited = {}
    return dp(max_num)


# T.O(m + n) M.O(n + k)
def del_earn(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    points = Counter(nums)

    for k, v in points.items():
        points[k] = k * v

    max_num = nums[0]
    for n in nums:
        max_num = max(max_num, n)

    num = 3
    dp_2 = points.get(num - 2, 0)
    dp_1 = points.get(num - 1, 0)

    while num <= max_num:
        dp_1, dp_2 = max(points.get(num, 0) + dp_2, dp_1), dp_1
        num += 1

    return dp_1


# T.O(n*logn) M.O(n)
def del_earn(nums: list[int]) -> int:

    nums.sort()
    points = Counter(nums)

    for k, v in points.items():
        points[k] = k * v

    keys = [k for k in points.keys()]

    if len(keys) == 1:
        return points[nums[0]]

    dp_2 = points[keys[0]]
    dp_1 = (
        max(points[keys[1]], dp_2)
        if keys[1] - keys[0] == 1
        else points[keys[0]] + points[keys[1]]
    )

    for i in range(2, len(keys)):

        if keys[i] - keys[i - 1] == 1:
            dp_1, dp_2 = max(points[keys[i]] + dp_2, dp_1), dp_1
        else:
            dp_1, dp_2 = points[keys[i]] + dp_1, dp_1

    return dp_1


if __name__ == "__main__":
    for test, expected in TESTS:
        result = del_earn(test)
        assert result == expected, (result, expected)
        print(f"Earned: {result} for {test}")
