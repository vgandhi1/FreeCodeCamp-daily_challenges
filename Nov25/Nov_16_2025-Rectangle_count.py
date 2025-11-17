"""
Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
"""
def count_rectangles(width, height):
    """
    Counts all possible sub-rectangles within a grid of size width x height.
    """
    
    # This list will store: ( (rectangle_size), count_of_that_size )
    pairs = []
    total_rectangle_count = 0

    # Loop through all possible RECTANGLE WIDTHS
    for w in range(1, width + 1):
        
        # Loop through all possible RECTANGLE HEIGHTS
        for h in range(1, height + 1):
            horizintal_rect_side = width - w + 1
            vertical_rect_side = height - h + 1

            count_of_rects = horizintal_rect_side*vertical_rect_side

            pairs.append(((w,h),count_of_rects))

            total_rectangle_count += count_of_rects

            
          
    #return total_rectangle_count, pairs
    return total_rectangle_count

# --- Test with (1, 3) ---
print(count_rectangles(1, 3))

# print("-" * 20)

# # --- Test with (2, 2) ---
print(count_rectangles(3, 2))


"""
Tests

Passed: 1. count_rectangles(1, 3) should return 6.
Passed: 2. count_rectangles(3, 2) should return 18.
Passed: 3. count_rectangles(1, 2) should return 3.
Passed: 4. count_rectangles(5, 4) should return 150.
Passed: 5. count_rectangles(11, 19) should return 12540.
"""


def count_rectangles_in_grid(width, height):
    """
    Counts all possible sub-rectangles within a grid of size width x height.
    """
    # Using integer division //
    horizontal_rects = (width * (width + 1)) // 2
    vertical_rects = (height * (height + 1)) // 2
    
    return horizontal_rects * vertical_rects

# For a 1x3 grid:
# horizontal = (1 * 2) // 2 = 1
# vertical = (3 * 4) // 2 = 6
# Total = 1 * 6 = 6

print(count_rectangles_in_grid(1, 3))
