"""
Credit Card Masker
Given a string of credit card numbers, return a masked version of it using the following constraints:

The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
Replace all numbers, except the last four, with an asterisk (*).
Leave the remaining characters unchanged.
For example, given "4012-8888-8888-1881" return "****-****-****-1881".
"""

def mask(card):
    last_4_digits = card[-4:]
    chars = [" ","-"]
    for char in chars:
        if char in card:
            return f"****{char}****{char}****{char}{last_4_digits}"
        
print(mask("4012-8888-8888-1881")) 
print(mask("5105 1051 0510 5100"))   

"""
1. mask("4012-8888-8888-1881") should return "****-****-****-1881".
Waiting:2. mask("5105 1051 0510 5100") should return "**** **** **** 5100".
Waiting:3. mask("6011 1111 1111 1117") should return "**** **** **** 1117".
Waiting:4. mask("2223-0000-4845-0010") should return "****-****-****-0010".
"""

import re

def mask(card: str) -> str:
    """
    Masks a credit card number string, replacing all digits except the 
    last four with an asterisk (*). Separators (space or hyphen) are preserved.
    
    The string is assumed to be in the format 'DDDD-DDDD-DDDD-DDDD' or 
    'DDDD DDDD DDDD DDDD'.
    """
    # 1. Separate the card into the part to mask and the last four digits.
    # The last four digits are preserved.
    last_4_digits = card[-4:]
    
    # The part to mask is everything up to the last four characters.
    part_to_mask = card[:-4]
    
    # 2. Use a regular expression to replace all digits (0-9) in the part_to_mask 
    # with an asterisk (*). This correctly preserves the separators.
    masked_part = re.sub(r'\d', '*', part_to_mask)
    
    # 3. Combine the masked part and the preserved last four digits.
    return masked_part + last_4_digits

# --- Test Cases ---
print(f'Test 1: {mask("4012-8888-8888-1881")}') 
print(f'Test 2: {mask("5105 1051 0510 5100")}') 
print(f'Test 3: {mask("6011 1111 1111 1117")}') 
print(f'Test 4: {mask("2223-0000-4845-0010")}')
