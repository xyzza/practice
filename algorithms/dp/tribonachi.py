TEST = [
    (0, 0),
    (1, 1),
    (2, 1),
    (4, 4),
    (25, 1389537),
]


# T.O(n) M.O(n)
def tribonacchi(n: int) -> int:
    def dp(i: int) -> int:
        if i in visited:
            return visited[i]

        if i == 0:
            res = 0
        elif i < 3:
            res = 1
        else:
            res = dp(i - 3) + dp(i - 2) + dp(i - 1)
        visited[i] = res
        return res

    visited = {}
    return dp(n)


# T.O(n) M.O(n)
def tribonacchi(n: int) -> int:

    if n == 0:
        return 0
    elif n < 3:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[-1]


# T.O(n) M.O(n)
def tribonacchi(n: int) -> int:

    if n == 0:
        return 0
    elif n < 3:
        return 1

    dp_i_0 = 0
    dp_i_1 = 1
    dp_i_2 = 1

    for i in range(3, n + 1):
        dp_i_1, dp_i_0, dp_i_2 = dp_i_2, dp_i_1, dp_i_2 + dp_i_1 + dp_i_0
    return dp_i_2


if __name__ == "__main__":
    for test, expected in TEST:
        result = tribonacchi(test)
        print(f"For n: {test} result: {result}")
        assert result == expected, (result, expected)
