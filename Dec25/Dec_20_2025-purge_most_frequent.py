"""
Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order.

"""
def purge_most_frequent(arr):

    if not arr:
        return []

    freq = dict()
    

    for a in arr:
        freq[a] = freq.get(a,0) + 1

    max_value = max(freq.values())


    return [i for i in arr if freq[i] != max_value ]


print(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]))

print(purge_most_frequent([1, 2, 2, 3]))

"""
Tests
Passed:1. purge_most_frequent([1, 2, 2, 3]) should return [1, 3].
Passed:2. purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]) should return ["a", "b", "b", "c", "c", "c"].
Passed:3. purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]) should return ["red", "green", "red", "green"].
Passed:4. purge_most_frequent([5, 5, 5, 5]) should return [].
"""
