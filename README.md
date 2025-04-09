# Maze Generation and Pathfinding

## Project Overview
This project implements a maze generation and recursive pathfinding algorithm in Python. The goal is to create a random, solvable maze and find a valid path from the start to the exit using a recursive depth-first search approach.

## Features
- Maze represented as a 2D grid (walls and paths)
- Configurable maze size (minimum 5x5)
- Maze generation using recursive backtracking
- Recursive DFS pathfinding algorithm
- Visual output of maze and solved path
- Graceful error handling for invalid inputs

## How to Use
1. Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
   
2. Save the Python code to a file, for example `maze.py`.

3. Run the program:
   ```bash
   python maze.py
Enter the desired number of rows and columns when prompted (e.g., 10 10).

Output Format
# — Wall

(space) — Open path

S — Start point (top-left corner)

E — Exit point (bottom-right corner)

. — Path taken from start to exit

Example output:

shell
Copy
Edit
##########
#S..#    #
###.#.## #
#   #.#  #
# ###.# ##
# #   #  #
# # ### ##
#     #E #
##########
Algorithm Explanation
Maze Generation (Recursive Backtracking)
Start from the start cell.

Randomly choose an unvisited neighbor 2 steps away.

Knock down the wall between the current cell and the neighbor.

Recursively continue until all reachable cells are visited.

Pathfinding (Recursive DFS)
Start at the start cell.

Recursively visit adjacent cells (up/down/left/right).

Mark visited paths.

Backtrack on dead ends.

Stop when the exit is reached.

Commit History 
Initial project setup

Maze class and basic structure

Implemented maze generation

Added random direction shuffle

Added recursive DFS for pathfinding

Implemented visited tracking

Added maze display function

Added user input and error handling

Final polishing and edge case checks

Updated README and documentation

Constraints
Only standard Python libraries used

Fully recursive pathfinding (no loops)

Guaranteed solvable maze

Author
[Saliev Yntymak] — April 2025
