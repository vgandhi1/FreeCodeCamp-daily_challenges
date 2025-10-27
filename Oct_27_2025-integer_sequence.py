"""
Integer Sequence
Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

For example, given 5, return "12345".
"""
# def sequence(n):
#     string = ''

#     for i in range(n):
#         string += f"{i+1}"


#     return string

# print(sequence(5))

# def sequence(n):
#     string = []

#     for i in range(n):
#         string.append(f"{i+1}")
        

#     return "".join(string)

# print(sequence(5))

def sequence(n):
           

    return "".join(str(i+1) for i in range(n))

print(sequence(5))


"""
Passed:1. sequence(5) should return "12345".
Passed:2. sequence(10) should return "12345678910".
Passed:3. sequence(1) should return "1".
Passed:4. sequence(27) should return "123456789101112131415161718192021222324252627".
"""
