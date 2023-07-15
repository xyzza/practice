"""
We have a bag of limited volume.
We have some stuff with cost and weight
Maximaze value in a bag
"""


items = {"water": 10, "book": 3, "food": 9, "jacket": 5, "camera": 6}

items_weight = {"water": 3, "book": 1, "food": 2, "jacket": 2, "camera": 1}

WEIGHT_LIMIT = 6

#         1   2   3   4   5   6
# water  |0   0   10  10  10  10
# book   |3   3   10  13  13  13
# food   |3   9   12  13  19  22
# jacket |3   9   12  14  19  22
# camera |6   9   15  18  19  25 (10 + 9 + 6)

# TODO: a bug?
# [0, 0, 10, 10, 10, 10]
# [3, 3, 10, 13, 13, 13]
# [0, 9, 12, 13, 19, 22]
# [0, 5, 12, 14, 19, 22]
# [6, 6, 12, 18, 20, 25]

#   1  2   3
#   0  1   2
# 0 [0, 10, 10] # first   v - 10 w - 2
# 1 [1, 10, 11] # second  v - 1 w - 1


# N items
# K weights
# N * K - combination of items
# start from first item
# [a..K] -> [0, 0, 0 ... /when item weight==k weight then val, val val]
# second item
# [b..K] -> [max(0, [a..k][j]), ... /when item weight==k then max([a..k][j], [b..k][j]), when item weight<k then max([b..k][j]+[a..k][k-weight], [a..k][j]+[b..k][k-weight])]


# table[1][2] = table[0][2]+table[1][0] # (10+1)
# i = 1 j = 2, wi = 1
# table[i][j] = table[i-1][j] + table[i][j-w]


def equip(values, weights, limit):

    equiped_items = []
    equiped_value = 0

    # to save order
    items = values.keys()

    table = [
        [
            values[item] if weights[item] <= lim else 0
            for lim in range(1, limit + 1)
        ]
        for item in items
    ]

    for i, item in enumerate(items):
        # item weight
        w = weights[item]

        for j, lim in enumerate(range(1, limit + 1)):

            addition = lim - w
            # max([b..k][j]+[a..k][k-weight], [a..k][j]+[b..k][k-weight])
            table[i][j] = max(
                table[i][j]
                if w == lim
                else 0,  # item itself, if sized in weight limit
                table[i - 1][j]
                if w == lim and i > 0
                else 0,  # previous item, if sized in weight limit
                table[i - 1][j] + table[i][addition]
                if lim > w
                else table[i][j],
            )
            # if i-1 >= 0 and lim-weights[item] >= 0:

            # table[i][j] = max(table[i][j] + table[i-1][lim-weights[item]], table[i-1][j])

        print(table[i])
    return table[len(table) - 1][len(table[0]) - 1]


# maximum affordable value must be 25 == 10 + 9 + 6
assert equip(items, items_weight, WEIGHT_LIMIT) == 25
