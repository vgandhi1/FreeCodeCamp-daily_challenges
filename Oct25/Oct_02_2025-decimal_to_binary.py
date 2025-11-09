"""
Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits 0 and 1 to represent any number. To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:

12 ÷ 2 = 6 remainder 0
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1
"""

def to_binary(decimal):
    intValue = int(decimal)
    
    binary = ""
   
    while intValue > 0:
        
        remainder = intValue % 2
        
        binary = str(remainder) + binary
        
        intValue = intValue//2

    return binary
    
print(to_binary("50"))

"""
//Test
Passed:1. to_binary(5) should return "101".
Passed:2. to_binary(12) should return "1100".
Passed:3. to_binary(50) should return "110010".
Passed:4. to_binary(99) should return "1100011".
"""
