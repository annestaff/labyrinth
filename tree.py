import math
import random


def prim(graph):
    C = {}
    P = {}
    for v in graph.nodes():
        C[v] = math.inf
        P[v] = {}

    Q = graph.nodes()

    while len(Q) != 0:
        u = (0, 0)
        # inf = math.inf
        i = math.inf
        for k in C:
            if C[k] < i and k in Q:
                i = C[k]
                u = k

        Q.remove(u)
        for v in graph.successors(u):
            if (v in Q) and (graph.arc_weight((u, v)) < C[v]):
                C[v] = random.random()  # graph.arc_weight((u,v))
                P[v] = u

    return P