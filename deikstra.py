from collections import deque

graph = {
    'BEGIN': [('A', 6), ('B', 2)],
    'A': [('END', 1)],
    'B': [('A', 3), ('END', 5)],
    'END': [],
    'NOWHERE': [],
}

graph2 = {
    'BEGIN': [('END', 100), ('B', 1)],
    'END': [],
    'B': [('END', 1)]
}


graph3 = {
    'BEGIN': [('END', 1), ('B', 100)],
    'END': [],
    'B': [('END', 100)]
}


def min_distance(graph, begin, end):
    """
    graph shoud be directed acyclic graph
    """
    routes = {k:'inf' for (k,v) in graph.items()}

    nodes = deque([(begin, graph[begin])])

    while nodes:

        root, _nodes = nodes.popleft()

        for (name, dist) in _nodes:
            # current length from begining to a node name
            _dist = routes[root] + dist if routes[root] != 'inf' else dist
            # if length ro a node name is not defined yet - define it
            if routes[name] != 'inf':
                routes[name] = min([routes[name], _dist])
            else:
                # else - choose which way is shorter - a new or old
                routes[name] = _dist
            
            nodes.append([name, graph[name]])

    return routes[end]


assert min_distance(graph, 'BEGIN', 'END') == 6
assert min_distance(graph2, 'BEGIN', 'END') == 2
assert min_distance(graph3, 'BEGIN', 'END') == 1
assert min_distance(graph, 'BEGIN', 'NOWHERE') == 'inf'