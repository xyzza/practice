INPUT = [4, 5, 1, 9, 0, 3, 4, 7, 1, 3, 9]
EXPECTED = sorted(INPUT)


def sort(sequence):
    n = len(sequence)
    result = [None] * n
    counts = [0] * n

    for el in sequence:
        counts[el] += 1

    for i in range(1, n):
        counts[i] += counts[i - 1]

    for el in sequence:
        counts[el] -= 1
        result[counts[el]] = el

    return result


if __name__ == "__main__":
    res = sort(INPUT)
    assert EXPECTED == res, (res, EXPECTED)
