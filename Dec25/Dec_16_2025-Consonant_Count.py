"""
Consonant Count
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.
"""
def has_consonant_count(text, target):
   # consonants = ["a", "e", "i", "o", "u"]
    consonants = {"a", "e", "i", "o", "u"}
    counter = 0
    for letter in text:
        if letter.isalpha():
            if letter.lower() not in consonants:
                counter += 1

    return counter == target

print(has_consonant_count("helloworld", 7))

"""
Tests
Passed:1. has_consonant_count("helloworld", 7) should return True.
Passed:2. has_consonant_count("eieio", 5) should return False.
Passed:3. has_consonant_count("freeCodeCamp Rocks!", 11) should return True.
Passed:4. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24) should return False.
Passed:5. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23) should return True.
"""
