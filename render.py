import math
import matplotlib.pyplot as plot


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


def draw_square_maze(graph, path=None, draw_coordinates=False):
    if path is None:
        path = []
    for u in graph.nodes():
        x, y = u

        if draw_coordinates:
            plot.text(x, y, str(x) + ', ' + str(y),
                      verticalalignment='center',
                      horizontalalignment='center')

        neighbours = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]

        for v in [s for s in neighbours if s not in graph.successors(u)]:
            draw_square_wall(u, v)

    for k in range(len(path) - 1):
        x1, y1 = path[k]
        x2, y2 = path[k + 1]
        plot.gca().add_line(plot.Line2D((x1, x2), (y1, y2), color='r'))

    plot.axis('scaled')
    plot.show()


def draw_hex_maze(graph, path=None, draw_coordinates=False):
    if path is None:
        path = []
    for u in graph.nodes():
        x, y = u

        if draw_coordinates:
            xt, yt = graph_to_hex_grid(u)
            plot.text(xt, yt, str(x) + ', ' + str(y),
                      verticalalignment='center',
                      horizontalalignment='center')

        if y % 2 == 0:
            neighbours = [(x + 1, y), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                          (x - 1, y + 1), (x, y + 1)]
        else:
            neighbours = [(x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y),
                          (x + 1, y + 1), (x, y + 1)]
        for v in [s for s in neighbours if s not in graph.successors(u)]:
            draw_hex_wall(u, v)

    for k in range(len(path) - 1):
        x1, y1 = graph_to_hex_grid(path[k])
        x2, y2 = graph_to_hex_grid(path[k + 1])
        plot.gca().add_line(plot.Line2D((x1, x2), (y1, y2), color='r'))

    plot.axis('scaled')
    plot.show()


def draw_line(u, v, color=None):
    xu, yu = u
    xv, yv = v
    plot.gca().add_line(plot.Line2D((xu, xv), (yu, yv), color=color))


def draw_node_box(u, color=None):
    x, y = u
    draw_line((x - .5, y - .5), (x + .5, y - .5), color)
    draw_line((x - .5, y + .5), (x + .5, y + .5), color)
    draw_line((x + .5, y - .5), (x + .5, y + .5), color)
    draw_line((x - .5, y - .5), (x - .5, y + .5), color)


def draw_node_box_corners(u, color=None):
    x, y = u
    draw_line((x - .5, y - .5), (x - .5, y - .5), color)
    draw_line((x - .5, y + .5), (x - .5, y + .5), color)
    draw_line((x + .5, y - .5), (x + .5, y - .5), color)
    draw_line((x - .5, y - .5), (x - .5, y - .5), color)


def draw_square_wall(u, v, color=None):
    xu, yu = u
    xv, yv = v
    xm, ym = ((xu + xv) / 2, (yu + yv) / 2)

    a = (xm + (ym - yu), ym + (xm - xu))
    b = (xm - (ym - yu), ym - (xm - xu))

    draw_line(a, b, color)


# The hexagon flat to flat diameter is 1. As such the horizontal distance
# between 2 nodes is always 1.
# The vertical distance is the long flat side of a triangle of small side 0.5
# and hypothenus 1.0. v^2 + 0.5^2 = 1.0^2, so v = sqrt( 1 - 0.25 ) = sqrt( 3/4 ).
# Every odd layer is offset by 0.5.

horizontal_distance = 1
vertical_distance = math.sqrt(3 / 4)
horizontal_offset = .5


def graph_to_hex_grid(u):
    x, y = u
    return x + (horizontal_offset if y % 2 == 1 else 0), y * vertical_distance


# the ratio from the flat radius r to get the side t is 2 / sqrt(3)

radius_to_side_ratio = 2 / math.sqrt(3)


def rotate_vector(v, angle, scale=1.):
    x, y = v
    return ((x * math.cos(angle) - y * math.sin(angle)) * scale,
            (x * math.sin(angle) + y * math.cos(angle)) * scale)


def draw_hex_wall(u, v, color=None):
    xu, yu = graph_to_hex_grid(u)
    xv, yv = graph_to_hex_grid(v)

    xm, ym = ((xu + xv) / 2, (yu + yv) / 2)

    #     a
    # u   m   v
    #     b

    a = rotate_vector((xv - xm, yv - ym), math.pi / 2, radius_to_side_ratio / 2)
    b = rotate_vector((xu - xm, yu - ym), math.pi / 2, radius_to_side_ratio / 2)

    xa, ya = a
    xb, yb = b

    draw_line((xa + xm, ya + ym), (xb + xm, yb + ym), color)