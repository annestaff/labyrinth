from game import Game
from maze import Maze


if __name__ == '__main__':
    print("Use the arrow keys to move along the maze. Press ESC to stop the game.")
    new_game = Game((20, 20))
    new_game.play()
