"""
Pairwise
Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

2 and 8 (2 + 8 = 10), whose indices are 0 and 4
4 and 6 (4 + 6 = 10), whose indices are 2 and 3
Add all the indices together to get a return value of 9.
"""
def pairwise(arr, target):

    indices = []
    n = len(arr)

    for i in range(n):
        for j in range(n):
            if i != j:
                if arr[i] + arr[j] == target:
                    indices.append((i, j))

    return sum(item[0] for item in indices)

print(pairwise([2, 3, 4, 6, 8], 10))

"""
ests
Passed:1. pairwise([2, 3, 4, 6, 8], 10) should return 9.
Passed:2. pairwise([4, 1, 5, 2, 6, 3], 7) should return 15.
Passed:3. pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20) should return 22.
Passed:4. pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24) should return 10.
"""


def pairwise(arr, target):
    used_indices = set()
    total_indices_sum = 0
    
    n = len(arr)
    
    for i in range(n):
        # Skip if this index was already paired
        if i in used_indices:
            continue
            
        for j in range(i + 1, n): # Start from i+1 to avoid self-pairing and double-counting
            # Skip if this index was already paired
            if j in used_indices:
                continue
            
            if arr[i] + arr[j] == target:
                total_indices_sum += (i + j)
                # Mark these as used so they aren't picked again
                used_indices.add(i)
                used_indices.add(j)
                # Once i is paired, break the inner loop to move to the next available i
                break
                
    return total_indices_sum
