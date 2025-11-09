"""
Hidden Treasure
Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

Each cell in the 2D array will contain one of the following values:

"-": No treasure.
"O": A part of the treasure that has not been found.
"X": A part of the treasure that has already been found.
If the dive location has no treasure, return "Empty".

If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

If the dive location finds the last unfound part of the treasure, return "Recovered".

For example, given:

[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.
"""

def dive(map, coordinates):
    # 1. Unpack coordinates
    row, col = coordinates
    
    # 2. Get the current location's content
    dive_location = map[row][col]
    
    # 3. Check for "Empty" case
    if dive_location == "-":
        return "Empty"
    
    unfound_treasure_part = 0

    for row in map:
        for i in row:
            if i == "O":
                unfound_treasure_part += 1
    if  unfound_treasure_part == 1 and dive_location == "O":
        return "Recovered"
    else:
        return "Found"

print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]))

print(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))

"""
1. dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) should return "Recovered".
Waiting:2. dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) should return "Empty".
Waiting:3. dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) should return "Found".
Waiting:4. dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) should return "Found".
Waiting:5. dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) should return "Recovered".
Waiting:6. dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) should return "Empty".
"""


