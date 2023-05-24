from math import inf

TESTS = [([6, 5, 4, 3, 2, 1], 2, 7), ([9, 9, 9], 4, -1), ([1, 1, 1], 3, 3)]


def main(costs: list[int], days: int) -> int:

    if len(costs) < days:
        return -1

    costs_cache = [0] * len(costs)
    hardest = 0
    for k in range(len(costs) - 1, -1, -1):
        costs_cache[k] = max(hardest, costs[k])
        hardest = costs_cache[k]
    visited = {}

    def dp(i, day):
        if (i, day) in visited:
            return visited[(i, day)]

        if day == days:
            res = costs_cache[i]
        else:
            # how much we can take? days - day
            # offset = days - day
            end = len(costs) - (days - day)

            res = inf
            hardest = 0
            for j in range(i, end):
                hardest = max(hardest, costs[j])
                res = min(dp(j + 1, day + 1) + hardest, res)
        visited[(i, day)] = res
        return res

    return dp(0, 1)


def main(costs: list[int], days: int) -> int:

    n = len(costs)

    if n < days:
        return -1

    dp = [[inf] * (days + 1) for _ in range(n)]
    dp[-1][days] = costs[-1]

    for i in range(n - 2, -1, -1):
        dp[i][days] = max(dp[i + 1][days], costs[i])

    for d in range(days - 1, 0, -1):
        for i in range(d - 1, n - (days - d)):
            hardest = 0
            for j in range(i, n - (days - d)):
                hardest = max(hardest, costs[j])
                dp[i][d] = min(dp[i][d], dp[j + 1][d + 1] + hardest)

    return dp[0][1]


if __name__ == "__main__":
    for costs, ds, expected in TESTS:
        result = main(costs, ds)
        print("Costs:", costs, "Days:", ds)
        print("Min difficulty:", result)
        assert result == expected, (result, expected)
