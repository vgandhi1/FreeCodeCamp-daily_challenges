"""
Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
"""

import re

def count(s):
    """
    Counts the number of vowels and consonants in a given string.
    """
    # A set for fast O(1) lookups
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert the entire string to lowercase to handle case-insensitivity
    s_lower = s.lower()
    
    # Use regex to remove all non-word characters (punctuation, spaces, etc.)
    # This leaves only the letters.
    # \W+ matches one or more non-alphanumeric characters.
    all_letters = re.sub(r'\W+', '', s_lower)

    # Get the total count of all letters
    total_letter_count = len(all_letters)
    vowel_count = 0
    
    # Iterate over each character in the letters-only string
    for char in all_letters:
        # Check if the character is in our vowel set
        if char in vowel_set:
            vowel_count += 1

    # Consonants are the total letters minus the vowels
    consonant_count = total_letter_count - vowel_count
    
    return [vowel_count, consonant_count]

# --- Test Cases ---
print(f"'Hello, World!': {count('Hello, World!')}")
print(f"'Hello World': {count('Hello World')}")
print(f"'JavaScript': {count('JavaScript')}")
print(f"'Python': {count('Python')}")
print(f"'freeCodeCamp': {count('freeCodeCamp')}")
print(f"'The quick brown fox jumps over the lazy dog.': {count('The quick brown fox jumps over the lazy dog.')}")

"""
Expected Test Results:
1. count("Hello World") should return [3, 7].
2. count("JavaScript") should return [3, 7].
3. count("Python") should return [1, 5].
4. count("freeCodeCamp") should return [5, 7].
5. count("Hello, World!") should return [3, 7].
6. count("The quick brown fox jumps over the lazy dog.") should return [11, 24].
"""
