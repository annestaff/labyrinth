from game import Game
from maze import Maze


if __name__ == '__main__':
    print("Welcome to the maze! Sit back, have a drink, and try to find the shortest exit.")
    print("\nUse the arrow keys to move along the maze. Press ESC to stop the game.")
    print("------------------------------------------------------------------------")
    new_game = Game((10, 10))
    new_game.play()
    next_game = input("\nWould you like to play the next level? (y/n)")
    game_cnt = 1
    while "y" in next_game:
        game_cnt += 1
        new_game = Game((10*game_cnt, 10*game_cnt))
        new_game.play()
        next_game = input("\nWould you like to play the next level? (y/n) ")
    print("\nBye bye 👋🏻")
