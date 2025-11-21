"""
Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.
"""
import re

def longest_word(sentence):
    clean_text = re.sub(r'[^\w\s]', '', sentence)
    words = clean_text.split(" ")
    n = 0
    for word in words:
        if len(word) > n:
            n = len(word)
            longest_word = word



    return longest_word

print(longest_word("The quick red fox"))
print(longest_word("Do Try This At Home."))

"""
Tests
Passed:1. longest_word("The quick red fox") should return "quick".
Passed:2. longest_word("Hello coding challenge.") should return "challenge".
Passed:3. longest_word("Do Try This At Home.") should return "This".
Passed:4. longest_word("This sentence... has commas, ellipses, and an exlamation point!") should return "exlamation".
Passed:5. longest_word("A tie? No way!") should return "tie".
Passed:6. longest_word("Wouldn't you like to know.") should return "Wouldnt".
"""
