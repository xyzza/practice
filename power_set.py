def foo(some_set: set) -> list:
    result = []
    if not some_set:
        return [some_set,]

    left = some_set.pop()
    left = set([left,])

    right = foo(set(some_set))

    for _r in right:
        if left:
            result.append(_r.union(left))
    result.extend(right)

    return result


res = foo(set(range(10)))
# Complexity is O(2^N)
print(len(res))