"""
Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".

"""

def speed_check(speed_mph, speed_limit_kph):
    speed_kph = speed_mph*1.60934

    speed_diff = speed_kph - speed_limit_kph

    if speed_diff <= 0:
        return "Not Speeding"
    if speed_diff <= 5:
        return "Warning"
    elif speed_diff > 5:
        return "Ticket"#, speed_diff

    


    

print(speed_check(30, 70))
print(speed_check(40, 60))
print(speed_check(65, 100))


"""
Tests
Waiting:1. speed_check(30, 70) should return "Not Speeding".
Waiting:2. speed_check(40, 60) should return "Warning".
Waiting:3. speed_check(40, 65) should return "Not Speeding".
Waiting:4. speed_check(60, 90) should return "Ticket".
Waiting:5. speed_check(65, 100) should return "Warning".
Waiting:6. speed_check(88, 40) should return "Ticket".
"""
