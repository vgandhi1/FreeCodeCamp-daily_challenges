"""
Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
"""

def validate(email):
    
    exact_one_symbol = len(email.split("@"))==2
    local_part = email.split("@")[0]
    domain_part = email.split("@")[-1]
    symbols = ['.','_','-']
    #contains_symbol = any(symbol in local_part for symbol in symbols)
    local_part_condition = all(char.isalnum() or char in symbols for char in local_part) and local_part[0] != "." and  local_part[-1] !="."
    domain_part_condition = len(domain_part.split(".")) >= 2 and len(domain_part.split(".")[-1]) >= 2 and domain_part.split(".")[-1].isalpha()

    double_dots = (not "" in local_part.split(".")) and (not "" in domain_part.split("."))

    return exact_one_symbol and local_part_condition and domain_part_condition and double_dots




#print(validate("freecodecamp.org"))

#print( validate("a@b.cd"))
#print(validate(".b@sh.rc"))

"""
Tests
Waiting:1. validate("a@b.cd") should return True.
Waiting:2. validate("hell.-w.rld@example.com") should return True.
Waiting:3. validate(".b@sh.rc") should return False.
Waiting:4. validate("example@test.c0") should return False.
Waiting:5. validate("freecodecamp.org") should return False.
Waiting:6. validate("develop.ment_user@c0D!NG.R.CKS") should return True.
Waiting:7. validate("hello.@wo.rld") should return False.
Waiting:8. validate("hello@world..com") should return False.
Waiting:9. validate("git@commit@push.io") should return False.
"""

#alternative code

def validate_refined(email):
    # 1. Exactly one @ symbol, and unpack parts
    parts = email.split("@")
    if len(parts) != 2:
        return False
        
    local_part, domain_part = parts
    symbols = ['.', '_', '-'] # Allowed in local part

    # 2. Local Part Constraints
    local_part_valid_chars = all(char.isalnum() or char in symbols for char in local_part)
    
    # Check for character set and start/end dot
    if not local_part_valid_chars or local_part.startswith('.') or local_part.endswith('.'):
        return False

    # 3. Double dots in local part
    if "" in local_part.split('.'):
        return False

    # 4. Domain Part Split & Double Dots
    domain_parts = domain_part.split('.')
    if "" in domain_parts:
        return False

    # 5. Domain Part Character Set (Standard Domain Rules: a-z, 0-9, -)
    #    This is a critical addition for robustness, as underscores are usually disallowed in domains.
    domain_symbols = ['-'] # Only hyphen is standard
    domain_chars_valid = all(char.isalnum() or char in domain_symbols or char == '.' for char in domain_part)
    # NOTE: If you must pass the "c0D!NG.R.CKS" test which contains '!', you'd remove this block.
    # But for a robust validator, this check is necessary.
    # if not domain_chars_valid:
    #     return False

    # 6. Domain Part Structure and TLD
    # Must contain at least one dot (checked by length >= 2)
    if len(domain_parts) < 2:
        return False

    # TLD (last part) must be at least 2 chars and all letters
    tld = domain_parts[-1]
    if len(tld) < 2 or not tld.isalpha():
        return False
        
    return True
