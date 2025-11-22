"""
LCM
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multiples of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.

"""
def lcm(a, b):

    if a == 0 or b == 0:
        return 0


    greatest = max(a,b)

    while True:
        if greatest%a == 0 and greatest%b == 0:
            return greatest
        
        greatest += max(a,b)
    
    
print(lcm(0, 0))
print(lcm(17, 13))
print(lcm(10, 100))


"""
Tests

Passed: 1. lcm(4, 6) should return 12.
Passed: 2. lcm(9, 6) should return 18.
Passed: 3. lcm(10, 100) should return 100.
Passed: 4. lcm(13, 17) should return 221.
Passed: 5. lcm(45, 70) should return 630.
"""
    
