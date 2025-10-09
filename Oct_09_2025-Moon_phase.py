"""
Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.
"""

from datetime import datetime
def moon_phase(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    reference_date_object = datetime.strptime("2000-01-06", '%Y-%m-%d')

    #date difference
    delta = abs((date_object-reference_date_object).days)

    
    
    moon_phase_remainder = (delta + 1)%28
    
    if 1 <= moon_phase_remainder <= 7:
        return "New"
    elif 8 <= moon_phase_remainder <= 14:
        return "Waxing"
    elif 15 <= moon_phase_remainder <= 21:
        return "Full"
    else: 
        return "Waning"

    #return date_string


"""
Passed:1. moon_phase("2000-01-12") should return "New".
Passed:2. moon_phase("2000-01-13") should return "Waxing".
Passed:3. moon_phase("2014-10-15") should return "Full".
Passed:4. moon_phase("2012-10-21") should return "Waning".
Passed:5. moon_phase("2022-12-14") should return "New".
"""

