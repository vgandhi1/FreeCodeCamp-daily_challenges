"""Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array.
"""


def find_landing_spot(matrix):
    landing_locations = []
    landing_locations_data = []
    #find location with zeros, a safe landing spot
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
             if element == 0:
                 landing_locations.append((i,j))
    
    for location in landing_locations:
        row, col = location
        neighbour_sum = 0
        
        neighbours = [(row - 1, col), (row + 1, col), 
                      (row, col - 1), (row, col + 1)]

        for neighbour in neighbours:
            i, j = neighbour
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]): 
                neighbour_sum += matrix[i][j]
        landing_locations_data.append((location,neighbour_sum))

    min_dangerous_val = min(landing_locations_data, key=lambda item: item[1])

    return list(min_dangerous_val[0])


"""
1. find_landing_spot([[1, 0], [2, 0]]) should return [0, 1].
Waiting:2. find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) should return [1, 1].
Waiting:3. find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) should return [2, 2].
Waiting:4. find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) should return [2, 1].
"""
"""
#alternative
def find_landing_spot(matrix):
    """
    Finds the safest landing spot for a rover in a matrix.
    
    The safest spot is a '0' cell with the lowest sum of its 
    four cardinal neighbors (up, down, left, right).
    
    Args:
        matrix: A list of lists representing potential landing spots.
        
    Returns:
        A list of two integers [row, col] representing the indices
        of the safest landing spot.
    """
    
    # Stores the coordinates and the neighbor sum for each potential landing spot
    safe_spots_with_danger = []

    # Get the dimensions of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Iterate through the matrix to find all potential landing spots (0s)
    for r in range(num_rows):
        for c in range(num_cols):
            if matrix[r][c] == 0:
                # Found a potential landing spot, now calculate its danger
                danger_sum = 0
                
                # Define the cardinal neighbor offsets: up, down, left, right
                neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

                # Sum the danger of the four neighbors
                for neighbor_r, neighbor_c in neighbors:
                    # Check if the neighbor is within the matrix boundaries
                    if 0 <= neighbor_r < num_rows and 0 <= neighbor_c < num_cols:
                        danger_sum += matrix[neighbor_r][neighbor_c]
                
                # Store the coordinates and the total danger
                safe_spots_with_danger.append(((r, c), danger_sum))
    
    # Find the tuple with the lowest danger sum
    # The `min()` function with a lambda key finds the element with the minimum
    # value at index 1 of the tuple.
    safest_spot_data = min(safe_spots_with_danger, key=lambda item: item[1])
    
    # The first element of the result is the coordinate tuple, convert it to a list
    safest_spot_coords = list(safest_spot_data[0])
    
    return safest_spot_coords
    """

