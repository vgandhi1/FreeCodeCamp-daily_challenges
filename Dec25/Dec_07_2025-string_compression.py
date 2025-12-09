"""
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".
"""

#from collections import Counter
def compress_string(sentence):
    words = sentence.split()

    freq = dict()
    #freq = Counter(split_sentence)

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    new_sentence = " ".join(f"{key}({value})" if value > 1 else f"{key}" for key, value in freq.items() )
        
    return new_sentence #split_sentence, freq

    #return new_sentence

print(compress_string("yes yes yes please"))
print(compress_string("I have have have apples"))
print(compress_string("one one three and to the the the the"))

"""
Tests
Waiting:1. compress_string("yes yes yes please") should return "yes(3) please".
Waiting:2. compress_string("I have have have apples") should return "I have(3) apples".
Waiting:3. compress_string("one one three and to the the the the") should return "one(2) three and to the(4)".
Waiting:4. compress_string("route route route route route route tee tee tee tee tee tee") should return "route(6) tee(6)
""" 
