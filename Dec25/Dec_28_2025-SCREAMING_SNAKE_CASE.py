"""
SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_)
"""
def to_screaming_snake_case(variable_name):
    x = [0]
    n = len(variable_name)
    words = []
    for idx, letter in enumerate(variable_name[1:]):
        if letter.isupper():
            x.append(idx+1)
    
    x.append(n)
    

    for i in range(len(x) - 1):
        
        word = variable_name[x[i]:x[i+1]]
        words.append(word)


    return "_".join(word.upper() for word in words).replace("-","_")

print(to_screaming_snake_case("UserPassword"))

"""
Tests
Passed:1. to_screaming_snake_case("userEmail") should return "USER_EMAIL".
Passed:2. to_screaming_snake_case("UserPassword") should return "USER_PASSWORD".
Passed:3. to_screaming_snake_case("user_id") should return "USER_ID".
Passed:4. to_screaming_snake_case("user-address") should return "USER_ADDRESS".
Passed:5. to_screaming_snake_case("username") should return "USERNAME".
"""
