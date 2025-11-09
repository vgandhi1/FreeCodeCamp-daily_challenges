"""
Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.
"""
def format(seconds):
    seconds = int(seconds)
    minutes = seconds//60
    final_second = seconds%60

    if  seconds > 3600 :
        hours = minutes//60
        minutes = (seconds-hours*3600)//60
        return f"{hours}:{minutes:02}:{final_second:02}"
    
    else:
        return f"{minutes}:{final_second:02}"
    


print(format(1))
print(format(4000))
print(format(5555))

print(format(99999))


"""
1. format(500) should return "8:20".
Passed:2. format(4000) should return "1:06:40".
Passed:3. format(1) should return "0:01".
Passed:4. format(5555) should return "1:32:35".
Passed:5. format(99999) should return "27:46:39".
"""

def format(total_seconds):
    # Ensure the input is an integer
    total_seconds = int(total_seconds)

    # Calculate hours, minutes, and seconds
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
       
    # Rule 3: Hours (H) should be included only if they're greater than zero.
    if hours > 0:
        
        return f"{hours}:{minutes:02}:{seconds:02}"
    
    # If hours is 0, the format is "MM:SS"
    else:
        
        return f"{minutes}:{seconds:02}"
