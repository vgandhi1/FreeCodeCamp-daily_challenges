"""
Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.
"""
def is_match(fingerprint_a, fingerprint_b):
    a = len(fingerprint_a)
    b = len(fingerprint_b)
    diff = 0
    if a == b:
        for i, j in zip(fingerprint_a,fingerprint_b):
            if i != j:
               diff += 1
        if diff <= 0.1*a:
            return True

    return False

"""
Tests
Waiting:1. is_match("helloworld", "helloworld") should return True.
Waiting:2. is_match("helloworld", "helloworlds") should return False.
Waiting:3. is_match("helloworld", "jelloworld") should return True.
Waiting:4. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") should return True.
Waiting:5. is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") should return True.
Waiting:6. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") should return False.
"""

def is_match_optimized(fingerprint_a, fingerprint_b):
    length = len(fingerprint_a)
    if length != len(fingerprint_b):
        return False
    
    limit = length * 0.1
    diff = 0
    
    for a, b in zip(fingerprint_a, fingerprint_b):
        if a != b:
            diff += 1
        # Early exit optimization
        if diff > limit:
            return False
            
    return True
