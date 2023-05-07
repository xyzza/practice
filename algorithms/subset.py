"""
"""

graph = {
    ("A", "B"): 10,
    ("B", "A"): 2,
    ("C", "A"): 5,
    ("A", "C"): 5,
    ("B", "C"): 10,
    ("C", "B"): 1,
}


def greedy_search(graph, path=None, length=0):

    if not graph:
        print(length)
        return path

    if path is None:
        path = []

    min_route = None
    min_distance = None

    for (route, distance) in graph.items():
        if min_route is None:
            min_route = route
            min_distance = distance

        if distance < min_distance:
            min_route = route
            min_distance = distance

    path.append(min_route)
    length += min_distance

    new_graph = {}
    for (route, distance) in graph.items():
        begin, end = route
        if begin == min_route[1] and end != min_route[0]:
            new_graph[route] = distance

    return greedy_search(new_graph, path, length=length)


print(greedy_search(graph))
