"""
Takeoff Fuel
Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

1 gallon equals 3.78541 liters.
If the airplane already has enough fuel, return 0.
You can only add whole gallons.
Do not include decimals in the return number.
"""
def fuel_to_add(current_gallons, required_liters):

    required_gallons = required_liters/3.78541
    #additional_gallons = 1

    if required_gallons <= current_gallons:
        additional_gallons = 0
        
    elif required_gallons < 1:
        additional_gallons = 1
    else:   
        additional_gallons = round(required_gallons) - current_gallons

    return additional_gallons

print(fuel_to_add(0, 1))

"""
Tests
Passed:1. fuel_to_add(0, 1) should return 1.
Passed:2. fuel_to_add(5, 40) should return 6.
Passed:3. fuel_to_add(10, 30) should return 0.
Passed:4. fuel_to_add(896, 20500) should return 4520.
Passed:5. fuel_to_add(1000, 50000) should return 12209.
# """

def fuel_to_add(current_gallons, required_liters):
    required_gallons = required_liters / 3.78541

    total_required_gallon = int(required_gallons)
    if required_gallons > total_required_gallon:
        total_required_gallon += 1

    additional_gallons = (int(required_gallons) + 1) - current_gallons

    return max(0, additional_gallons)

print(fuel_to_add(10, 30))
print(fuel_to_add(0, 1))
print(fuel_to_add(5, 40))
