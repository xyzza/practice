from itertools import permutations
INPUTS = (1,2,3,4,5,6)


def perm(inputs: tuple) -> list:
    result = []
    if len(inputs)<2:
        return [inputs]

    for index, _ in enumerate(inputs):
        left = inputs[index]
        right = perm(inputs[:index] + inputs[index+1:])
        for p in right:
            result.append((left,) + p)

    return result


assert perm(INPUTS) == [x for x in permutations(INPUTS)]
