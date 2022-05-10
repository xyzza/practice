TEST_DATA = (
    (
        [4, 9, 8, 3, 6, 0, 1, 5, 7, 2],
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
        ],
    ),
    (
        [4, 8, 3, 6, 0, 1, 5, 7, 2],
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
        ],
    ),
    (
        [4],
        [4],
    ),
    (
        [],
        [],
    ),
)


def merge_sort(data):

    def _merge(left, right):
        result = []
        while left and right:
            if right[-1] > left[-1]:
                result.append(right.pop())
            else:
                result.append(left.pop())
        if not right:
            result = left + result[::-1]
        else:
            result = right + result[::-1]
        return result

    length = len(data)
    if length < 2:
        return data
    middle = length // 2
    sorted_left = merge_sort(data[:middle])
    sorted_right = merge_sort(data[middle:])
    return _merge(sorted_left, sorted_right)


def main():
    for _input, expected in TEST_DATA:
        print(_input)
        result = merge_sort(_input)
        print(result)
        assert result == expected


if __name__ == "__main__":
    main()
