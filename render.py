import matplotlib.pyplot as plot
from matplotlib.patches import ConnectionPatch


def draw_tree(graph, draw_coordinates=False):
    for u in graph.nodes():
        x, y = u
        if draw_coordinates:
            plot.text(x, y, str(x) + ', ' + str(y),
                      verticalalignment='center',
                      horizontalalignment='center')
        for v in graph.successors(u):
            draw_line(u, v)
    plot.axis('scaled')
    plot.show()


def draw_line(u, v, color=None, line_width=1):
    xu, yu = u
    xv, yv = v
    plot.gca().add_line(plot.Line2D([xu, xv], [yu, yv], color=color, linewidth=line_width))


def draw_surroundings(u, v, color=None):
    xu, yu = u
    xv, yv = v
    xm = (xu + xv) / 2
    ym = (yu + yv) / 2
    a = [xm + (ym - yu), ym + (xm - xu)]
    b = [xm - (ym - yu), ym - (xm - xu)]
    draw_line(a, b, color)


def draw_path(path=None):
    if path is None or len(path) < 2:
        plot.gca().plot(0, 0, "ro")
    else:
        for u in range(1, len(path)):
            draw_line(path[u-1], path[u], color="red", line_width=4)
