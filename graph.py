import random


class Graph:
    def __init__(self, width, height):
        self.adjacency = {}
        self.weights = {}
        self.width = width
        self.height = height
        for k in range(0, width):
            for j in range(0, height):
                if j + 1 <= height - 1:
                    self.add_edge(((k, j), (k, j + 1)), random.random())
                if k + 1 <= width - 1:
                    self.add_edge(((k, j), (k + 1, j)), random.random())

    def __str__(self):
        return "adjacency : " + str(self.adjacency) + " \nweights : " + str(self.weights)

    def add_node(self, s):
        if s in self.adjacency:
            return
        self.adjacency[s] = set()

    def add_edge(self, edge, weight=1.0):
        s1, s2 = edge
        self.add_node(s1)
        self.add_node(s2)
        self.weights[edge] = weight
        self.adjacency[s1].add(s2)

    def nodes(self):
        return set(self.adjacency)

    def neightbours(self, node):
        return set(self.adjacency[node])

    def edge_weight(self, edge):
        return self.weights[edge]

    def set_edge_weight(self, edge, weight):
        self.weights[edge] = weight
