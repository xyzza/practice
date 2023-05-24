from functools import lru_cache
from math import inf

TESTS = [
    ([1, 2, 5], 11, 3),
    (
        [
            2,
        ],
        3,
        -1,
    ),
    ([1], 0, 0),
]


def main(coins: list[int], amount: int) -> int:
    @lru_cache(2000)
    def dp(i) -> int:

        if i == 0:
            res = 0
        elif i < 0:
            res = -1
        else:
            options = [dp(i - c) for c in coins]
            res = min([it for it in options if it >= 0], default=-1)
            return res + 1 if res >= 0 else -1

        return res

    r = dp(amount)
    return r if r != inf else -1


if __name__ == "__main__":
    for coins, amount, expected in TESTS:
        result = main(coins, amount)
        print(f"Coins: {coins} | Amount: {amount}")
        assert result == expected, (result, expected)
