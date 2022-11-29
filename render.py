import matplotlib.pyplot as plot


def draw_line(u, v, color=None, line_width=1):
    xu, yu = u
    xv, yv = v
    plot.gca().add_line(plot.Line2D([xu, xv], [yu, yv], color=color, linewidth=line_width))


def draw_wall(u, v, color=None):
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
            if path[u] in path[:u]:
                colour = "black"
            else:
                colour = "red"
            draw_line(path[u-1], path[u], color=colour, line_width=4)
