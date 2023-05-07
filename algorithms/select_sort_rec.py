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


def select_sort_rec(data, length):
    if not length:
        return data
    for i, el in enumerate(data[:length]):
        if el > data[length - 1]:
            data[length - 1], data[i] = data[i], data[length - 1]
    select_sort_rec(data, length - 1)
    return data


def main():
    for _input, expected in TEST_DATA:
        print(_input)
        result = select_sort_rec(_input, len(_input))
        print(result)
        assert result == expected


if __name__ == "__main__":
    main()
