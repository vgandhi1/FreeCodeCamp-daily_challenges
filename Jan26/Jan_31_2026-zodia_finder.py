"""
Zodiac Finder
Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date using the following chart:

Date Range	        Zodiac Sign
March 21 - April 19	"Aries"
April 20 - May 20	"Taurus"
May 21 - June 20	"Gemini"
June 21 - July 22	"Cancer"
July 23 - August 22	"Leo"
August 23 - September 22	"Virgo"
September 23 - October 22	"Libra"
October 23 - November 21	"Scorpio"
November 22 - December 21	"Sagittarius"
December 22 - January 19	"Capricorn"
January 20 - February 18	"Aquarius"
February 19 - March 20	"Pisces"
Zodiac signs are based only on the month and day, you can ignore the year.

"""
from datetime import date

def get_sign(date_str):
    ZODIAC_RANGES = [
    ((3, 21),  (4, 19),  "Aries"),
    ((4, 20),  (5, 20),  "Taurus"),
    ((5, 21),  (6, 20),  "Gemini"),
    ((6, 21),  (7, 22),  "Cancer"),
    ((7, 23),  (8, 22),  "Leo"),
    ((8, 23),  (9, 22),  "Virgo"),
    ((9, 23),  (10, 22), "Libra"),
    ((10, 23), (11, 21), "Scorpio"),
    ((11, 22), (12, 21), "Sagittarius"),
    ((12, 22), (1, 19),  "Capricorn"),  # wraps year
    ((1, 20),  (2, 18),  "Aquarius"),
    ((2, 19),  (3, 20),  "Pisces"),
    ]

    target = date.fromisoformat(date_str)
    month_day = (target.month, target.day)

    for start, end, zodiac_sign in ZODIAC_RANGES:
        start_month, start_day = start
        end_month, end_day = end

        if end_month < start_month: # wraps year condition
            if month_day >=  start or month_day <= end:
                return zodiac_sign

        else:
            if start <= (target.month, target.day) <= end:
                return zodiac_sign

    return None


    #return target.month, target.day
"""
Tests
Passed:1. get_sign("2026-01-31") should return "Aquarius".
Passed:2. get_sign("2001-06-10") should return "Gemini".
Passed:3. get_sign("1985-09-07") should return "Virgo".
Passed:4. get_sign("2023-03-19") should return "Pisces".
Passed:5. get_sign("2045-11-05") should return "Scorpio".
Passed:6. get_sign("1985-12-06") should return "Sagittarius".
Passed:7. get_sign("2025-12-30") should return "Capricorn".
Passed:8. get_sign("2018-10-08") should return "Libra".
Passed:9. get_sign("1958-05-04") should return "Taurus".
"""
