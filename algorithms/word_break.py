from functools import lru_cache

TEST = [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    (
        "catsandog",
        ["cats", "cat", "sand", "and", "dog"],
        False,
    ),
]


def main(s: str, wordDict: list[str]) -> bool:
    n = len(s)

    dp = [False] * n

    for i in range(n):
        for w in wordDict:
            w_start = i - (len(w) - 1)
            if s[w_start : i + 1] == w and (w_start - 1 < 0 or dp[w_start - 1]):
                dp[i] = True
                break

    return dp[-1]


def main(s: str, wordDict: list[str]):
    @lru_cache
    def dp(i: int) -> bool:

        if i < 0:
            return True
        for w in wordDict:
            if s[i - len(w) + 1 : i + 1] == w and dp(i - len(w)):
                return True

        return False

    return dp(len(s) - 1)


if __name__ == "__main__":
    for test_case in TEST:
        _s, _dict, expected = test_case
        result = main(_s, _dict)
        print(f"For s:{_s} and dict: {_dict} result:", result)
        assert result == expected, (result, expected)
