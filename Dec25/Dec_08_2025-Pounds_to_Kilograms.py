"""
Pounds to Kilograms
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".

"""
def convert_to_kgs(lbs):

    kg = lbs*0.453592 

    if lbs == 1:
        return f"{lbs} pound equals {kg:.2f} kilograms."

    if round(kg,2) == 1.00:
        return f"{lbs} pounds equals {kg:.2f} kilogram."


    return f"{lbs} pounds equals {kg:.2f} kilograms."

print(convert_to_kgs(1))

print(convert_to_kgs(2.20462))

print(convert_to_kgs(2.5))
print(.453592*2.20462)

"""
Tests
Passed:1. convert_to_kgs(1) should return "1 pound equals 0.45 kilograms.".
Failed:2. convert_to_kgs(0) should return "0 pounds equals 0.00 kilograms.".
Passed:3. convert_to_kgs(100) should return "100 pounds equals 45.36 kilograms.".
Passed:4. convert_to_kgs(2.5) should return "2.5 pounds equals 1.13 kilograms.".
Passed:5. convert_to_kgs(2.20462) should return "2.20462 pounds equals 1.00 kilogram.".
"""

def convert_to_kgs(lbs):

    kg = lbs*0.453592 
    kg_formatted = f"{kg:.2f}"

    lb_unit = "pounds"
    kg_unit = "kilograms"

    if lbs == 1:
        lb_unit = "pound"
    if kg_formatted == "1.00":
        kg_unit = "kilogram"
        
    
    return f"{lbs} {lb_unit} equals {kg_formatted} {kg_unit}."
