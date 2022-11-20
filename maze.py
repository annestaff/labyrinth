from graph import Graph
import matplotlib.pyplot as plot

from render import draw_tree, draw_square_maze
from tree import prim


def create_graph(width, height):
    G1 = Graph()
    for k in range(0, width):
        for j in range(0, height):
            if j + 1 <= height - 1:
                G1.add_arc(((k, j), (k, j + 1)))
            if k + 1 <= width - 1:
                G1.add_arc(((k, j), (k + 1, j)))
    return G1


class Maze(Graph):
    def __init__(self, width, height):
        super().__init__()
        self.graph = create_graph(width, height)

    def draw_tree(self):
        draw_tree(self.graph, True)

    def generate_labyrinth(self):
        P = prim(self.graph)
        G2 = Graph()
        for key in P:
            value = P[key]
            if value == {}:
                continue
            G2.add_arc((key, value))
            G2.add_arc((value, key))
        self.graph = G2

    def draw_square_maze(self):
        draw_square_maze(self.graph)
