"""
Sum the String
Given a string containing digits and other characters, return the sum of all numbers in the string.

Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
Ignore any non-digit characters.
"""
def string_sum(s):
    total_string_sum = []
    current_num_in_string = ""

    for ch in s:
        if ch.isdigit():
            current_num_in_string += ch

        else:
            if current_num_in_string:
                current_number = int(current_num_in_string)
                total_string_sum.append(current_number)
                current_num_in_string = ""
    if current_num_in_string:
        current_number = int(current_num_in_string)
    total_string_sum.append(current_number)

    return  sum(total_string_sum)

print(string_sum("125344"))
print(string_sum("10cats5dogs2birds"))
print(string_sum("3apples2bananas"))
print(string_sum("a1b20c300"))
print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))

