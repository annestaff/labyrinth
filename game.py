from pynput.keyboard import Key, Listener
from maze import Maze
import matplotlib.pyplot as plot

from render import draw_path


MOVEMENTS = {
    Key.right: (1, 0),
    Key.left: (-1, 0),
    Key.up: (0, 1),
    Key.down: (0, -1)
}


class Game:
    def __init__(self, size):
        width, height = size
        self.maze = Maze(width, height)
        self.maze.generate_labyrinth()
        self.path = [(0, 0)]
        self.position = (0, 0)

    def read_movement(self, key):
        if key == Key.esc:
            return False
        if key not in MOVEMENTS:
            print("Invalid movement. To stop the game, press ESC.")
        else:
            self.move_by(MOVEMENTS[key])

    def move_by(self, u):
        x, y = self.position
        x += u[0]
        y += u[1]
        if (x, y) in self.maze.graph.successors(self.position):
            self.path.append((x, y))
            self.position = (x, y)
        self.update_plot()

    def move_to(self, u):
        if u in self.maze.graph.successors(self.position):
            self.path.append(u)
            self.position = u
        self.update_plot()

    def update_plot(self):
        self.maze.draw_maze(path=self.path)

    def play(self):
        with Listener(on_press=self.read_movement) as listener:
            listener.join()
