"""
Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
"""

def has_exoplanet(readings):

    list_value = []

    for char in readings:
        if char.isdigit():
            val = int(char)
            
        elif char.isalpha():
            val = ord(char) - ord("A") + 10
        
        list_value.append(val)

    avg_value = sum(list_value)/len(list_value)
    threshold = 0.8
    threshold_value = threshold*avg_value

    return any( val <= threshold_value for val in list_value)


"""
Passed:1. has_exoplanet("665544554") should return False.
Passed:2. has_exoplanet("FGFFCFFGG") should return True.
Passed:3. has_exoplanet("MONOPLONOMONPLNOMPNOMP") should return False.
Passed:4. has_exoplanet("FREECODECAMP") should return True.
Passed:5. has_exoplanet("9AB98AB9BC98A") should return False.
Passed:6. has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") should return True.
"""
