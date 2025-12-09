"""
Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.
"""
def most_frequent(arr):
    freq = dict()

    for item in arr:
        if item in freq:
            freq[item] = freq.get(item,0) + 1
        else:
            freq[item] = 1

    sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)

    return sorted_freq[0][0]

print(most_frequent(["a", "b", "a", "c"]))
print(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]))
print(most_frequent([True, False, "False", "True", False]))

"""
Tests
Passed:1. most_frequent(["a", "b", "a", "c"]) should return "a".
Passed:2. most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) should return 2.
Passed:3. most_frequent([True, False, "False", "True", False]) should return False.
Passed:4. most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) should return 40.
"""

def most_frequent_optimized(arr):
    # 1. Count Frequencies (O(M) time)
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1

    # 2. Find the Max Frequency Element (O(N) time, N is unique elements)
    # The problem guarantees a single most frequent element,
    # so we don't need to worry about ties.
    
    # Initialize trackers
    max_count = 0
    most_frequent_element = None

    # Iterate through the frequency map
    for element, count in freq.items():
        if count > max_count:
            max_count = count
            most_frequent_element = element
    
    return most_frequent_element

# Example Tests
print(most_frequent_optimized(["a", "b", "a", "c"])) # Expected: "a"
print(most_frequent_optimized([2, 3, 5, 2, 6, 3, 2, 7, 2, 9])) # Expected: 2
print(most_frequent_optimized([True, False, "False", "True", False])) # Expected: False

