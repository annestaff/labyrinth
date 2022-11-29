import math


def spanning_tree(graph):
    cost = {}
    previous = {}
    for v in graph.nodes():
        cost[v] = math.inf
        previous[v] = {}
    queue = graph.nodes()
    while len(queue) != 0:
        u = (0, 0)
        i = math.inf
        for k in cost:
            if cost[k] < i and k in queue:
                i = cost[k]
                u = k
        if u in queue:
            queue.remove(u)
        for v in graph.neightbours(u):
            if (v in queue) and (graph.edge_weight((u, v)) < cost[v]):
                cost[v] = graph.edge_weight((u, v))
                previous[v] = u
    return previous
