from graph import Graph
import matplotlib.pyplot as plot

from render import draw_wall, draw_path
from spanning_tree import spanning_tree


class Maze(Graph):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.path = None
        self.generate_labyrinth()

    def generate_labyrinth(self):
        tree = spanning_tree(self)
        self.adjacency = {}
        self.weights = {}
        for u in tree:
            v = tree[u]
            if v != {}:
                self.add_edge((u, v))
                self.add_edge((v, u))
        is_path_found = False
        path = [(self.width - 1, self.height - 1)]
        while not is_path_found:
            path.append(tree[path[-1]])
            if path[-1] == (0, 0):
                is_path_found = True
        path.reverse()
        self.path = path

    def draw_maze(self, path=None, draw_coordinates=False):
        plot.ion()
        for u in self.nodes():
            x, y = u
            if draw_coordinates:
                plot.text(x, y, str(x) + ', ' + str(y),
                          verticalalignment='center',
                          horizontalalignment='center')
            neighbours = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
            for v in [s for s in neighbours if s not in self.successors(u)]:
                draw_wall(u, v)
        plot.text(-1, -0.3, "Start here -->", horizontalalignment='right', verticalalignment='bottom')
        plot.text(self.width, self.height-1, "<-- Exit", horizontalalignment='left', verticalalignment='bottom')
        draw_path(path)
        plot.axis('scaled')
        plot.axis('off')
        plot.show(block=False)
