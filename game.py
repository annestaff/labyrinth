from pynput.keyboard import Key, Listener
from maze import Maze


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
        self.maze.draw_maze()
        self.path = [(0, 0)]
        self.position = (0, 0)
        self.is_win = False
        self.score = 0

    def read_movement(self, key):
        if key == Key.esc:
            return False
        if key not in MOVEMENTS:
            print("Invalid movement. To stop the game, press ESC.")
        else:
            self.move_by(MOVEMENTS[key])
        if self.is_win:
            return False

    def move_by(self, u):
        x, y = self.position
        x += u[0]
        y += u[1]
        if (x, y) in self.maze.neightbours(self.position):
            self.path.append((x, y))
            self.position = (x, y)
        else:
            print("You can't go through walls.")
        self.update_plot()
        if self.position == (self.maze.width-1, self.maze.height-1):
            self.is_win = True

    def update_plot(self):
        self.maze.draw_maze(path=self.path)

    def calculate_score(self):
        self.score = len(self.maze.path)/len(self.path)*100

    def play(self):
        with Listener(on_press=self.read_movement) as listener:
            listener.join()
        print("------------------------------------------------------------------------")
        if self.is_win:
            self.calculate_score()
            if self.score == 100.0:
                print("\nBravo, perfect game! Your score is 100/100 🎉")
            elif 80.0 <= self.score < 100.0:
                print("\nNicely done! Your score is ", int(self.score), "/100 👏🏻")
            elif 50.0 < self.score < 80.0:
                print("\nNot shabby at all. Your score is ", int(self.score), "/100 🙌🏻")
            else:
                print("\nWell, let's say at least you made it. Your score is ", int(self.score), "/100 😅")
        else:
            print("\nToo bad you didn't make it. Maybe next time 😇")
