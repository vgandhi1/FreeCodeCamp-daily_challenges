"""Hex to Decimal
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

0-9 represent values 0 through 9.
A-F represent values 10 through 15.
Here's a partial conversion table:

"""

def hex_to_decimal(hex):
    n = len(hex)
    char_val = []
    decimal = 0

    for char in hex:
        if char.isdigit():
            char = int(char)
        elif char.isalpha():
            char = ord(char) - ord('A') + 10
        else:
            print("invalid entry")
        char_val.append(char)

    for i in range(n):
        value = (16**i)*char_val[-(i+1)]
        decimal += value


    return decimal


#alternative way

def hex_to_decimal(hex_str: str) -> int:
    # Remove leading "0x" if present
    hex_str = hex_str.strip().upper().replace("0X", "")
    
    decimal_value = 0
    power = 0
    
    # Process from right to left
    for char in reversed(hex_str):
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - ord('A') + 10  # Convert A-F to 10-15
        decimal_value += value * (16 ** power)
        power += 1
    
    return decimal_value


#easier way to handle it

def hex_to_decimal(hex_str):
    try:
        # Remove '0x' or '0X' prefix if present
        if hex_str.lower().startswith('0x'):
            hex_str = hex_str[2:]
        return int(hex_str, 16)
    except (ValueError, TypeError):
        print("Invalid hexadecimal input.")
        return None


"""

1. hex_to_decimal("A") should return 10.
2. hex_to_decimal("15") should return 21.
3. hex_to_decimal("2E") should return 46.
4. hex_to_decimal("FF") should return 255.
5. hex_to_decimal("A3F") should return 2623.
"""





