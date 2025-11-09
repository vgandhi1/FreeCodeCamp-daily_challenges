"""
String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
"""


def count(text, parameter):
    n = len(parameter)
    counter = 0
    for i in range(len(text) + 1 - n):
        if text[i: i+n] == parameter:
            counter += 1  
        
    return counter

"""
Waiting:1. count('abcdefg', 'def') should return 1.
Waiting:2. count('hello', 'world') should return 0.
Waiting:3. count('mississippi', 'iss') should return 2.
Waiting:4. count('she sells seashells by the seashore', 'sh') should return 3.
Waiting:5. count('101010101010101010101', '101') should return 10.
"""
