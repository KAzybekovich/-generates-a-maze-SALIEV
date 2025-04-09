import random

WALL = '#'
PATH = ' '
VISITED = '.'

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Maze:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.grid = [[WALL for _ in range(cols)] for _ in range(rows)]
        self.visited = [[False for _ in range(cols)] for _ in range(rows)]
        self.start = Cell(1, 1)
        self.exit = Cell(rows - 2, cols - 2)
        self.generate_maze(self.start.row, self.start.col)

    def generate_maze(self, r, c):
        directions = [Cell(-2, 0), Cell(2, 0), Cell(0, -2), Cell(0, 2)]
        self.grid[r][c] = PATH
        random.shuffle(directions)

        for dir in directions:
            nr, nc = r + dir.row, c + dir.col
            if self.is_in_bounds(nr, nc) and self.grid[nr][nc] == WALL:
                self.grid[r + dir.row // 2][c + dir.col // 2] = PATH
                self.generate_maze(nr, nc)

    def is_in_bounds(self, r, c):
        return 0 < r < self.rows - 1 and 0 < c < self.cols - 1

    def solve_maze(self, r, c):
        if not self.is_in_bounds(r, c) or self.grid[r][c] != PATH or self.visited[r][c]:
            return False
        self.visited[r][c] = True

        if r == self.exit.row and c == self.exit.col:
            self.grid[r][c] = VISITED
            return True

        if (self.solve_maze(r + 1, c) or self.solve_maze(r - 1, c) or
            self.solve_maze(r, c + 1) or self.solve_maze(r, c - 1)):
            self.grid[r][c] = VISITED
            return True

        return False

    def display_maze(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i == self.start.row and j == self.start.col:
                    print('S', end='')
                elif i == self.exit.row and j == self.exit.col:
                    print('E', end='')
                else:
                    print(self.grid[i][j], end='')
            print()

def main():
    try:
        r, c = map(int, input("Enter maze size (rows cols): ").split())
        if r < 5 or c < 5:
            print("Invalid size. Maze must be at least 5x5.")
            return

        maze = Maze(r, c)
        print("Generated Maze:")
        maze.display_maze()

        if maze.solve_maze(1, 1):
            print("\nSolved Maze with path:")
            maze.display_maze()
        else:
            print("\nNo path found from start to exit.")
    except ValueError:
        print("❌ Please enter two integers separated by space (e.g., 10 10)")

if __name__ == "__main__":
    main()
