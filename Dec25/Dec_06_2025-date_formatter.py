"""
Date Formatter
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06".
"""
def format_date(date_string):

    month_to_number = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }

    month_str, day_str, year = date_string.split()

    #mm_string = date_string.split(" ")[0]
    mm = month_to_number.get(month_str)
    dd = int(day_str.replace(",",""))
    #year = date_string.split(" ")[-1]

    return f"{year}-{mm:02}-{dd:02}"

print(format_date("December 6, 2025"))
print(format_date("January 1, 2000"))

"""
Tests

Passed: 1. format_date("December 6, 2025") should return "2025-12-06".
Passed: 2. format_date("January 1, 2000") should return "2000-01-01".
Passed: 3. format_date("November 11, 1111") should return "1111-11-11".
Passed: 4. format_date("September 7, 512") should return "512-09-07".
Passed: 5. format_date("May 4, 1950") should return "1950-05-04".
Passed: 6. format_date("February 29, 1992") should return "1992-02-29".
"""
