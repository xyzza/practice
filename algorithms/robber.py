"""
Robber may rob every house on the street, but adjusted houses will trigger the alarm.
Find the maximum price of goods that may be collected without triggering alarm
"""


TESTS = [
    ([2, 7, 9, 3, 0, 0, 0, 0, 1000], 1011),
    ([2, 7, 9, 3, 1], 12),
    ([2, ], 2),
    ([], 0),
    ([2,1,1,2], 4),
]


# Top to bottom with memoization
# T.O(n) M.O(n)
def robber(nums: list[int]) -> int:

    if len(nums) < 2:
        return nums[0] if nums else 0

    visited = {}

    def dp(n):
        if tuple(n) in visited:
            return visited[tuple(n)]
        if len(n) == 1:
            res = n[0]
        elif len(n) == 0:
            res = 0
        else:
            res = max(dp(n[1:]), dp(n[2:]) + n[0])
        visited[tuple(n)] = res
        return res

    return dp(nums)


# Bottom up
# T.O(n) M.O(1) inplace
def robber(nums: list[int]) -> int:

    if len(nums) < 2:
        return nums[0] if nums else 0

    s_2 = nums[0]
    s_1 = max(s_2, nums[1])

    for i in range(2, len(nums)):
        s_1, s_2 = max(nums[i] + s_2, s_1), s_1

    return s_1


if __name__ == "__main__":
    for test, expected in TESTS:
        result = robber(test)
        print(f"Goods price: {result}")
        assert result == expected, result
