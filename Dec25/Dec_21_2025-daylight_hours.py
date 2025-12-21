"""
Daylight Hours
December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.

Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:

Latitude	Daylight Hours
-90	24
-75	23
-60	21
-45	15
-30	13
-15	12
0	12
15	11
30	10
45	9
60	6
75	2
90	0
If the given latitude does not exactly match a table entry, use the value of the closest latitude.
"""
def daylight_hours(latitude):
    day_light_hours = {
        -90: 24, -75: 23, -60: 21, -45: 15, -30: 13, -15: 12,
        0: 12, 15: 11, 30: 10, 45: 9, 60: 6, 75: 2, 90: 0
    }

    dist = float("inf")

    for lat in day_light_hours.keys():
        lat_dist = abs(lat - latitude)

        if lat_dist < dist:
            dist = lat_dist
            closest_lat  = lat


    #closest_lat = min(day_light_hours.keys(), key = lambda x: abs(x - latitude))

    return day_light_hours[closest_lat]

print(daylight_hours(45))

"""
Tests
Passed:1. daylight_hours(45) should return 9.
Passed:2. daylight_hours(0) should return 12.
Passed:3. daylight_hours(-90) should return 24.
Passed:4. daylight_hours(-10) should return 12.
Passed:5. daylight_hours(23) should return 10.
Passed:6. daylight_hours(88) should return 0.
Passed:7. daylight_hours(-33) should return 13.
Passed:8. daylight_hours(70) should return 2.
"""

