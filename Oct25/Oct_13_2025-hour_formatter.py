"""
24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

"""
def to_12(time):
    hour = int(time[0:2])
    minute = (time[2:])

    if hour == 0:
            return f"12:{minute} AM"
    elif hour < 12:
        return f"{hour}:{minute} AM"
    else:
        remainder = hour%12
        return f"{remainder}:{minute} PM"

def to_12(time):
    hour = int(time[0:2])
    minute = time[2:]

    # Determine AM or PM
    meridiem = "AM"
    if hour >= 12:
        meridiem = "PM"

    # Convert hour to 12-hour format
    if hour == 0:
        hour = 12
    elif hour > 12:
        hour -= 12

    return f"{hour}:{minute} {meridiem}"

  """
  Tests
Waiting:1. to_12("1124") should return "11:24 AM".
Waiting:2. to_12("0900") should return "9:00 AM".
Waiting:3. to_12("1455") should return "2:55 PM".
Waiting:4. to_12("2346") should return "11:46 PM".
Waiting:5. to_12("0030") should return "12:30 AM".
"""
