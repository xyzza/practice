from random import randint


def qsort(collection):
    if len(collection)<1:
        return []
    main = collection[-1]
    left = [el for el in collection[:-1] if el < main]
    right = [el for el in collection[:-1] if el >= main]
    return qsort(left) + [main,] + qsort(right)


rand_sample = [randint(-100, 100) for _ in range(20)]
assert qsort([2,3,1]) == [1,2,3]
assert qsort([2,2,1,1,0]) == [0,1,1,2,2]
assert qsort(rand_sample) == sorted(rand_sample)