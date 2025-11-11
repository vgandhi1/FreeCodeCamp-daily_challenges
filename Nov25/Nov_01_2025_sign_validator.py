"""
Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
Check if the computed signature matches the provided signature.
"""
def verify(message, key, signature):

    def calc(words):
        words_sum = []
        for word in words:
            if word.isalpha():
                if word.isupper():
                    word_val = ord(word) - ord('A') + 27
                else:
                    word_val = ord(word) - ord('a') + 1

            else:
                word_val = 0
            words_sum.append(word_val)
            
        return words_sum

    message_key_sum = sum(calc(message) + calc(key)) 


    return message_key_sum == signature

print(verify("foo", "bar", 57))


"""
Passed:1. verify("foo", "bar", 57) should return True.
Passed:2. verify("foo", "bar", 54) should return False.
Passed:3. verify("freeCodeCamp", "Rocks", 238) should return True.
Passed:4. verify("Is this valid?", "No", 210) should return False.
Passed:5. verify("Is this valid?", "Yes", 233) should return True.
Passed:6. verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) should return True.
"""

def verify_signature(message, key, signature):
    """
    Verifies a signature by summing the character values of a message and a key.
    """

    def calculate_string_sum(text_string):
        """
        Calculates the total value of a string based on the defined rules:
        a-z: 1-26
        A-Z: 27-52
        Other: 0
        """
        total_sum = 0
        for char in text_string:
            if 'a' <= char <= 'z':
                # a-z map to 1-26
                total_sum += ord(char) - ord('a') + 1
            elif 'A' <= char <= 'Z':
                # A-Z map to 27-52
                total_sum += ord(char) - ord('A') + 27
            # Non-alphabetic characters add 0, so we can just ignore them
        
        return total_sum

    # Calculate the sum for the message and the key
    computed_signature = calculate_string_sum(message) + calculate_string_sum(key)

    # Compare with the provided signature
    return computed_signature == signature

# --- Test Cases ---
print(f"'foo', 'bar', 57: {verify_signature('foo', 'bar', 57)}") # True
print(f"'freeCodeCamp', 'Rocks', 238: {verify_signature('freeCodeCamp', 'Rocks', 238)}") # True
print(f"'Is this valid?', 'Yes', 233: {verify_signature('Is this valid?', 'Yes', 233)}") # True
print(f"'Is this valid?', 'No', 210: {verify_signature('Is this valid?', 'No', 210)}") # False
