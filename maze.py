import random

from graph import Graph
import matplotlib.pyplot as plot

from render import draw_tree, draw_surroundings, draw_path
from spanning_tree import spanning_tree


def create_graph(width, height):
    res = Graph()
    for k in range(0, width):
        for j in range(0, height):
            if j + 1 <= height - 1:
                res.add_edge(((k, j), (k, j + 1)), random.random())
            if k + 1 <= width - 1:
                res.add_edge(((k, j), (k + 1, j)), random.random())
    return res


class Maze(Graph):
    def __init__(self, width, height):
        super().__init__()
        self.graph = create_graph(width, height)
        self.width = width
        self.height = height

    def draw_tree(self):
        draw_tree(self.graph, True)

    def generate_labyrinth(self):
        tree = spanning_tree(self.graph)
        res = Graph()
        for u in tree:
            v = tree[u]
            if v == {}:
                continue
            res.add_edge((u, v))
            res.add_edge((v, u))
        self.graph = res

    def draw_maze(self, path=None, draw_coordinates=False):
        plot.ion()
        for u in self.graph.nodes():
            x, y = u
            if draw_coordinates:
                plot.text(x, y, str(x) + ', ' + str(y),
                          verticalalignment='center',
                          horizontalalignment='center')
            neighbours = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
            for v in [s for s in neighbours if s not in self.graph.successors(u)]:
                draw_surroundings(u, v)
        draw_path(path)
        plot.axis('scaled')
        plot.axis('off')
        plot.show(block=False)
