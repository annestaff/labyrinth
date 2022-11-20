from maze import Maze

if __name__ == '__main__':
    maze1 = Maze(10, 10)
    maze1.draw_tree()
    maze1.generate_labyrinth()
    maze1.draw_tree()
    maze1.draw_square_maze()
