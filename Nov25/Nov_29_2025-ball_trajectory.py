"""
Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.
"""
def get_next_location(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                i_1, j_1 = i, j
            if matrix[i][j] == 2:
                i_2, j_2 = i, j

    delta_i = i_2 - i_1
    delta_j = j_2 - j_1

    if (i_2 == 0 and delta_i == -1 ) or (i_2 == (len(matrix) -1) and delta_i == 1):
        delta_i = -1*delta_i
    if (j_2 == 0 and delta_j == -1 ) or (j_2 == (len(matrix[0]) -1 ) and delta_j == 1):
        delta_j = -1*delta_j

    return [i_2 + delta_i, j_2 + delta_j]

print(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]))

print(get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]))

"""
Tests
Passed:1. get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) should return [2, 3].
Passed:2. get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) should return [3, 0].
Passed:3. get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) should return [1, 2].
Passed:4. get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) should return [1, 1].
Passed:5. get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) should return [2, 2].
"""
def get_next_location(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    # Find previous and current positions
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                i_1, j_1 = i, j
            if matrix[i][j] == 2:
                i_2, j_2 = i, j
    
    # Movement deltas
    delta_i = i_2 - i_1
    delta_j = j_2 - j_1

    # Bounce off top/bottom walls
    if i_2 + delta_i < 0 or i_2 + delta_i >= rows:
        delta_i = -delta_i

    # Bounce off left/right walls
    if j_2 + delta_j < 0 or j_2 + delta_j >= cols:
        delta_j = -delta_j

    return [i_2 + delta_i, j_2 + delta_j]
