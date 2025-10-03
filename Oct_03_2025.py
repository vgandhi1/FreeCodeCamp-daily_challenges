def check_strength(password):
    """
    Evaluates password strength based on four rules:
    - Length >= 8 characters
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*)
    
    Args:
        password (str): The password string to evaluate.
        
    Returns:
        str: "weak", "medium", or "strong".
    """
    condition_sum = 0
    special_chars = '!@#$%^&*'

    # Rule 1: At least 8 characters long
    if len(password) >= 8:
        condition_sum += 1

    # Rule 2: Contains both uppercase and lowercase letters
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        condition_sum += 1
    
    # Rule 3: Contains at least one digit
    if any(char.isdigit() for char in password):
        condition_sum += 1

    # Rule 4: Contains at least one special character
    if any(char in special_chars for char in password):
        condition_sum += 1

    if condition_sum == 4:
        return "strong"
    elif condition_sum >= 2:
        return "medium"
    else:
        return "weak"


"""
Tests
Waiting:1. check_strength("123456") should return "weak".
Waiting:2. check_strength("pass!!!") should return "weak".
Waiting:3. check_strength("Qwerty") should return "weak".
Waiting:4. check_strength("PASSWORD") should return "weak".
Waiting:5. check_strength("PASSWORD!") should return "medium".
Waiting:6. check_strength("PassWord%^!") should return "medium".
Waiting:7. check_strength("qwerty12345") should return "medium".
Waiting:8. check_strength("PASSWORD!") should return "medium".
Waiting:9. check_strength("PASSWORD!") should return "medium".
Waiting:10. check_strength("S3cur3P@ssw0rd") should return "strong".
Waiting:11. check_strength("C0d3&Fun!") should return "strong".
"""
