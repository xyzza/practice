"""
We have a bag of limited volume.
We have some stuff with cost and weight
Maximaze value in a bag
"""


items = {
    'water': 10,
    'book': 3,
    'food': 9,
    'jacket': 5,
    'camera': 6
}

items_weight = {
    'water': 3,
    'book': 1,
    'food': 2,
    'jacket': 2,
    'camera': 1
    
}

WEIGHT_LIMIT = 6

#         1   2   3   4   5   6
# water  |0   0   10  10  10  10
# book   |3   3   10  13  13  13
# food   |0   9   12  13  19  22
# jacket |0   9   12  14  19  22
# camera |6   9   15  18  19  25 (10 + 9 + 6)

# TODO: a bug?
# [0, 0, 10, 10, 10, 10]
# [3, 3, 10, 13, 13, 13]
# [0, 9, 12, 13, 19, 22]
# [0, 5, 12, 14, 19, 22]
# [6, 6, 12, 18, 20, 25]



def equip(values, weights, limit):

    equiped_items = []
    equiped_value = 0

    
    # to save order
    items = values.keys()

    table = [
        [
            values[item] if weights[item] <= lim else 0 
            for lim in range(1, limit+1)
        ] 
        for item in items
    ]

    for i, item in enumerate(items):
        for lim in range(limit):
            if i -1 >= 0 and lim-weights[item] >= 0:

                table[i][lim] = max(table[i][lim] + table[i-1][lim-weights[item]], table[i-1][lim])

        print(table[i])
    return table[len(table)-1][len(table[0])-1]

# maximum affordable value must be 25 == 10 + 9 + 6
assert equip(items, items_weight, WEIGHT_LIMIT) == 25
