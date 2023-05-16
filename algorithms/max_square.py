TESTS = [
    (
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        4,
    ),
    ([["0", "1"], ["1", "0"]], 1),
    ([["0"]], 0),
    (
        [
            ["1", "0", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "1", "1"],
            ["0", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "0", "1", "0"],
            ["0", "1", "1", "1", "1", "1"],
            ["1", "1", "0", "1", "1", "1"],
        ],
        4,
    ),
]


def max_square(matrix: list[list[str]]) -> int:
    M = matrix
    n = len(M[0])
    m = len(M)
    visited = {}

    def dp(i: int, j: int) -> int:

        if (i, j) in visited:
            return visited[(i, j)]

        if i >= m or j >= n:
            res = 0
        elif M[i - 1][j - 1] == "1":
            res = 1 + min(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1))
        else:
            res = 0

        visited[(i, j)] = res
        return res

    dp(m, n)
    r = max(visited.values())
    return r * r


def max_square(matrix: list[list[str]]) -> int:
    M = matrix
    n = len(M[0])
    m = len(M)

    _max = 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if M[i - 1][j - 1] == "1":
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                _max = max(_max, dp[i][j])

    return _max**2


if __name__ == "__main__":
    for test, expected in TESTS:
        result = max_square(test)
        assert result == expected, f"{result=}, {expected=}"
        print(f"Max square of {test} is: {result}")
