"""
FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".
"""
def fizz_buzz(n):
    int_array = []
    
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            i = "FizzBuzz"
        elif i%5 == 0:
            i = "Buzz"
        elif i%3 == 0:
            i = "Fizz"
        int_array.append(i)

    return int_array

print(fizz_buzz(20))

"""
Tests
Passed:1. fizz_buzz(2) should return [1, 2].
Passed:2. fizz_buzz(4) should return [1, 2, "Fizz", 4].
Passed:3. fizz_buzz(8) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8].
Passed:4. fizz_buzz(20) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"].
Passed:5. fizz_buzz(50) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"].
"""

def fizz_buzz(n):
    """
    Returns an array of integers from 1 to n (inclusive), 
    replacing multiples of 3 with "Fizz", 5 with "Buzz", and 3 and 5 with "FizzBuzz".
    """
    return [
        "FizzBuzz" if i % 15 == 0 else  # Check for 3 and 5 (i.e., 15) first
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        i  # Default case if no other conditions are met
        for i in range(1, n + 1)
    ]

# Example Usage
print(fizz_buzz(20))
