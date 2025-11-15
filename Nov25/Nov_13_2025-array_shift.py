"""
Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
"""
def shift_array(arr, n):
    m = len(arr)
    final_arr = [0]*m
    for i, val in enumerate(arr):
        new_i = (i - n)%(m)
        final_arr[new_i] = val

    return final_arr

print(shift_array([1, 2, 3], 1))

"""
Tests

Passed: 1. shift_array([1, 2, 3], 1) should return [2, 3, 1].
Passed: 2. shift_array([1, 2, 3], -1) should return [3, 1, 2].
Passed: 3. shift_array(["alpha", "bravo", "charlie"], 5) should return ["charlie", "alpha", "bravo"].
Passed: 4. shift_array(["alpha", "bravo", "charlie"], -11) should return ["bravo", "charlie", "alpha"].
Passed: 5. shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) should return [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
"""
