"""
What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.
"""
from datetime import date

def calculate_age(birthday: str) -> int:
    birthYear, birthMonth, birthDay = map(int, birthday.split("-"))
    current_date = date.today() #date(2025, 11, 27)

    age = current_date.year - birthYear

    if (birthMonth, birthDay) > (current_date.month, current_date.day):
        age -= 1
    

    return age#, current_date

print(calculate_age("2000-11-29"))

"""
Tests
Passed:1. calculate_age("2000-11-20") should return 25.
Passed:2. calculate_age("2000-12-01") should return 24.
Passed:3. calculate_age("2014-10-25") should return 11.
Passed:4. calculate_age("1994-01-06") should return 31.
Passed:5. calculate_age("1994-12-14") should return 30.
"""
