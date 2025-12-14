"""
Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.

"""
def game_of_life(grid):
    R = len(grid)
    C = len(grid[0])

    n_status = dict()

    new_grid = [[0 for j in range(C)] for i in range(R)]

    for i in range(R):
        for j in range(C):
            e = (i, j)
            
            sum_ = 0
            
            neighbours = [(i, j-1), (i-1, j-1), (i-1, j), (i-1,j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1)]
            for neighbour in neighbours:
                x, y = neighbour
                if 0 <= x < R and 0 <= y < C:
                    sum_ += grid[x][y]

                value = sum_

            n_status[e] = value

            if grid[i][j] == 1  and (n_status[e] < 2 or n_status[e] > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 1  and (n_status[e] == 2 or n_status[e] == 3):
                new_grid[i][j] = 1
            
            elif grid[i][j] == 0 and n_status[e] == 3:
                new_grid[i][j] = 1

            else:
                new_grid[i][j] = grid[i][j]




    return new_grid
print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
"""
Tests

Failed: 1. game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]) should return [[0, 1, 1], [0, 0, 1], [1, 1, 1]].
Failed: 2. game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]) should return [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]].
Failed: 3. game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) should return [[0, 0, 0], [0, 1, 0], [0, 0, 0]].
Failed: 4. game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]) should return [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]].
"""
