from collections import deque

graph = {
    "BEGIN": [("A", 6), ("B", 2)],
    "A": [("END", 1)],
    "B": [("A", 3), ("END", 5)],
    "END": [],
    "NOWHERE": [],
}

graph2 = {"BEGIN": [("END", 100), ("B", 1)], "END": [], "B": [("END", 1)]}


graph3 = {"BEGIN": [("END", 1), ("B", 100)], "END": [], "B": [("END", 100)]}


def min_distance(graph, begin, end):
    """
    graph shoud be directed acyclic graph
    """
    routes = {k: "inf" for (k, v) in graph.items()}

    nodes = deque([(begin, graph[begin])])

    while nodes:

        root, _nodes = nodes.popleft()

        for (name, dist) in _nodes:
            # current length from begining to a node name
            _dist = routes[root] + dist if routes[root] != "inf" else dist
            # if length ro a node name is not defined yet - define it
            if routes[name] != "inf":
                routes[name] = min([routes[name], _dist])
            else:
                # else - choose which way is shorter - a new or old
                routes[name] = _dist

            nodes.append([name, graph[name]])

    return routes[end]


assert min_distance(graph, "BEGIN", "END") == 6
assert min_distance(graph2, "BEGIN", "END") == 2
assert min_distance(graph3, "BEGIN", "END") == 1
assert min_distance(graph, "BEGIN", "NOWHERE") == "inf"


# alternate realisation

graph = {
    "BEGIN": {"A": 6, "B": 2},
    "A": {"END": 1, "END2": 100},
    "B": {"A": 3, "END": 5},
    "END": {},
    "END2": {},
}


from collections import defaultdict


def search(graph, parent, children, costs, paths):

    for node, cost in children.items():
        from_parent_cost = costs[parent] + cost
        if from_parent_cost == float("inf"):
            costs[node] = cost
            paths[node] = parent
        elif from_parent_cost < costs[node]:
            costs[node] = from_parent_cost
            paths[node] = parent
        search(graph, node, graph[node], costs, paths)

    return costs, paths


costs, paths = search(
    graph,
    "BEGIN",
    graph["BEGIN"],
    defaultdict(lambda: float("inf")),
    dict(),
)
assert costs["END"] == 6
print(costs)
tail = "END"
while tail in paths:
    print(tail)
    tail = paths[tail]
