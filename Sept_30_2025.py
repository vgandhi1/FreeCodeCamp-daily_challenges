"""
Phone Number Formatter
Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
"""
def format_number(number):
    #if isdigit(number):
    countryCode = number[0]
    areaCode = number[1:4]
    middle = number[4:7]
    last = number[7:11]
    formattedNumber = f'+{countryCode} ({areaCode}) {middle}-{last}'


    return formattedNumber

"""
Passed: 1. format_number("05552340182") should return "+0 (555) 234-0182".
Passed: 2. format_number("15554354792") should return "+1 (555) 435-4792".
"""
