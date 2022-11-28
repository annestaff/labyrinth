class Graph:
    def __init__(self):
        self.adjacency = {}
        self.weights = {}

    def __str__(self):
        return "adjacency : " + str(self.adjacency) + " \nweights : " + str(self.weights)

    def add_node(self, s):
        if s in self.adjacency:
            return
        self.adjacency[s] = set()

    def add_edge(self, edge, weight=1):
        s1, s2 = edge

        self.add_node(s1)
        self.add_node(s2)
        self.weights[edge] = weight
        self.adjacency[s1].add(s2)

    def remove_edge(self, edge):
        if edge not in self.weights:
            return
        del self.weights[edge]
        s1, s2 = edge
        self.adjacency[s1].remove(s2)

    def remove_node(self, node):
        if node not in self.adjacency:
            return
        for other in self.adjacency:
            self.remove_edge((node, other))
            self.remove_edge((other, node))
        del self.adjacency[node]

    def nodes(self):
        return set(self.adjacency)

    def successors(self, node):
        return set(self.adjacency[node])

    def predecessors(self, node):
        return set(s for s in self.adjacency if s in self.adjacency[node])

    def edge_weight(self, edge):
        return self.weights[edge]

    def set_edge_weight(self, edge, weight):
        self.weights[edge] = weight
