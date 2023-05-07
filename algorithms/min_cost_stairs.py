"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
"""

TESTS = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([], 0),
    ([1], 0),
]


# T.O(n) M.O(n)
def climb(cost: list[int]) -> int:
    def dp(i):
        if i in visited:
            return visited[i]

        if i < 2:
            res = 0
        elif i == 3:
            res = min(cost[i - 1], cost[i - 2])
        else:
            res = min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2))
        visited[i] = res
        return res

    visited = {}
    return dp(len(cost))


# T.O(n) M.O(1)
def climb(cost: list[int]) -> int:

    dp_i_1 = dp_i_2 = 0

    for i in range(2, len(cost) + 1):
        dp_i_1, dp_i_2 = min(cost[i - 1] + dp_i_1, cost[i - 2] + dp_i_2), dp_i_1

    return dp_i_1


if __name__ == "__main__":
    for test, expected in TESTS:
        result = climb(test)
        print(f"Price is : {result}")
        assert result == expected, (result, expected)
