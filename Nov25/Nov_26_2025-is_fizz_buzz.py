"""
BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements.
"""
def is_fizz_buzz(sequence):

    int_array = []
    n = len(sequence)
    
    for i in range(1, n + 1):
        if i%15 == 0:
            i = "FizzBuzz"
        elif i%5 == 0:
            i = "Buzz"
        elif i%3 == 0:
            i = "Fizz"
        int_array.append(i)

    return int_array == sequence

print(is_fizz_buzz([1, 2, "Fizz", 4]))

"""
Tests

Passed: 1. is_fizz_buzz([1, 2, "Fizz", 4]) should return True.
Passed: 2. is_fizz_buzz([1, 2, 3, 4]) should return False.
Passed: 3. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) should return False.
Passed: 4. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]) should return False.
Passed: 5. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]) should return False.
Passed: 6. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]) should return False.
Passed: 7. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]) should return True.
"""

#alternative code
def is_fizz_buzz(sequence):
    """
    Validates the sequence by checking each element against its expected value.
    Returns False immediately if an error is found.
    """
    l = []
    n = len(sequence)
    

    for i in range(1, n + 1):
        expected = ""
        if i%3 == 0:
            expected += "Fizz"
        if i%5 == 0:
            expected += "Buzz"
        
        if not expected:
            expected = i

        l.append(expected)

        if expected != sequence[i-1]:
            return False

    return True

# Example Usage
print(is_fizz_buzz([1, 2, "Fizz", 4]))

#or better way

def is_fizz_buzz(sequence):
    """
    Validates the sequence by checking each element against its expected value.
    Returns False immediately if an error is found.
    """
    l = []
    n = len(sequence)
    

    for i in range(1, n + 1):
        expected = ""
        if i%15 == 0:
            expected = "FizzBuzz"
        elif i%3 == 0:
            expected = "Fizz"
        elif i%5 == 0:
            expected = "Buzz"
        else:
            expected = i

        l.append(expected)

        if expected != sequence[i-1]:
            return False

    return True

# Example Usage
print(is_fizz_buzz([1, 2, "Fizz", 4]))