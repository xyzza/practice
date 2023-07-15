TESTS = [
    (("abcde", "ace"), 3),
    (("abc", "def"), 0),
    (("bsbininm", "jmjkbkjkv"), 1),
]


def max_common_subseq(text1: str, text2: str) -> int:

    t1 = len(text1)
    t2 = len(text2)
    visited = {}

    def dp(i: int, j: int) -> int:
        if (i, j) in visited:
            return visited[(i, j)]
        if i == t1 or j == t2:
            res = 0
        else:
            try:
                pos = text2.index(text1[i], j)
            except ValueError:
                pos = None

            if pos is None:
                res = dp(i + 1, j)
            else:
                res = max(dp(i + 1, j), 1 + dp(i + 1, pos + 1))
        visited[(i, j)] = res
        return res

    return dp(0, 0)


def max_common_subseq(text1: str, text2: str) -> int:
    t1 = len(text1)
    t2 = len(text2)
    visited = {}

    def dp(i: int, j: int) -> int:
        if (i, j) in visited:
            return visited[(i, j)]

        if i < 0 or j < 0:
            res = 0
        elif text1[i] == text2[j]:
            res = 1 + dp(i - 1, j - 1)
        else:
            res = max(dp(i - 1, j), dp(i - 1, j - 1))

        visited[(i, j)] = res
        return res

    return dp(t1 - 1, t2 - 1)


def max_common_subseq(text1: str, text2: str) -> int:
    t1 = len(text1)
    t2 = len(text2)

    dp = [[0] * (t1 + 1) for _ in range(t2 + 1)]

    for i in range(t1 - 1, -1, -1):
        for j in range(t2 - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[j][i] = 1 + dp[j + 1][i + 1]
            else:
                dp[j][i] = max(dp[j][i + 1], dp[j + 1][i])

    return dp[0][0]


if __name__ == "__main__":
    for test, expected in TESTS:
        result = max_common_subseq(*test)
        assert result == expected, (test, result, expected)
        print(f"Max common subseq of {test} is: {result}")
