"""
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.
"""
#import string
def title_case(title):
    title_list = title.lower().split(" ")
    


    return " ".join(word.capitalize() for word in title_list) #string.capwords(title)

print(title_case("hello world"))

"""
Tests

Passed: 1. title_case("hello world") should return "Hello World".
Passed: 2. title_case("the quick brown fox") should return "The Quick Brown Fox".
Passed: 3. title_case("JAVASCRIPT AND PYTHON") should return "Javascript And Python".
Passed: 4. title_case("AvOcAdO tOAst fOr brEAkfAst") should return "Avocado Toast For Breakfast".
"""
