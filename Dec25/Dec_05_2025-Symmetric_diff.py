"""
Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.
"""

def difference(arr1, arr2):
    diff = []
    for i in arr1:
        if i not in arr2:
            diff.append(i)
    for j in arr2:
        if j not in arr1:
            diff.append(j)


    return diff

print(difference([1, 2, 3], [3, 4, 5]))
print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""
Tests
Passed:1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
Passed:2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
Passed:3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
Passed:4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].

"""

def difference(arr1, arr2):
    diff = []
    seen = set()

    for x in arr1:
        if x not in arr2 and x not in seen:
            diff.append(x)
            seen.add(x)

    for x in arr2:
        if x not in arr1 and x not in seen:
            diff.append(x)
            seen.add(x)

    return diff


def difference(a, b):
    return [x for x in a + b if (x in a) ^ (x in b)]
