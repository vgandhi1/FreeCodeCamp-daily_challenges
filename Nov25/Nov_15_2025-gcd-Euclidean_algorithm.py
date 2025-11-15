"""
GCD
Given two positive integers, return their greatest common divisor (GCD).

The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
"""
def gcd(x, y):
    #int(max(x,y)%min(x,y))

    def divisor(n):
        divisor_list = []
        for i in range(1,n):
            if n%i == 0:
               divisor_list.append(i)

        return divisor_list

    all_divisor = list(set(divisor(x)) & set(divisor(y))) 


    return max(all_divisor)

print(gcd(654, 456))
print(gcd(13, 17))
print(gcd(20, 15))


"""
Tests

Passed: 1. gcd(4, 6) should return 2.
Passed: 2. gcd(20, 15) should return 5.
Passed: 3. gcd(13, 17) should return 1.
Passed: 4. gcd(654, 456) should return 6.
Passed: 5. gcd(3456, 4320) should return 864.
"""

def gcd(a, b):
    # This loop continues as long as b is not zero
    while b:  
        # This one line is the magic of the Euclidean algorithm.
        # It updates a to be the old b, and b to be the remainder of a / b.
        a, b = b, a % b
        
    # When the loop finishes, b is 0, and a holds the GCD
    return a
