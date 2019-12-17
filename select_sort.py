def select_sort(collection):

    if len(collection) == 1:
        return collection

    _max = collection[0]
    _max_index = 0

    for index, element in enumerate(collection):

        if element > _max:
            _max = element
            _max_index = index

    return select_sort(collection[:_max_index] + collection[_max_index+1:]) + [_max,]
