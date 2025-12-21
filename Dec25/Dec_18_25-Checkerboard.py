"""

Checkerboard
Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]

"""

def create_board(dimensions):
    m, n =dimensions

    checkerboard = []

    for i in range(m):
        raw_i = []
        for j in range(n):
            val = i + j
            if val%2 == 0:
                raw_i.append("X")
            else:
                raw_i.append("O")
        checkerboard.append(raw_i)
        
    return checkerboard

print(create_board([3, 3]))

"""
Tests
Waiting:1. create_board([3, 3]) should return [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]].
Waiting:2. create_board([6, 1]) should return [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]].
Waiting:3. create_board([2, 10]) should return [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]].
Waiting:4. create_board([5, 4]) should return [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]].
"""
