"""
Infected
On November 2nd, 1988, the first major internet worm was released, infecting about 10% of computers connected to the internet after only a day.

In this challenge, you are given a number of days that have passed since an internet worm was released, and you need to determine how many computers are infected using the following rules:

On day 0, the first computer is infected.
Each subsequent day, the number of infected computers doubles.
Every 3rd day, a patch is applied after the virus spreads and reduces the number of infected computers by 20%. Round the number of patched computers up to the nearest whole number.
For example, on:

Day 0: 1 total computer is infected.
Day 1: 2 total computers are infected.
Day 2: 4 total computers are infected.
Day 3: 8 total computers are infected. Then, apply the patch: 8 infected * 20% = 1.6 patched. Round 1.6 up to 2. 8 computers infected - 2 patched = 6 total computers infected after day 3.
Return the number of total infected computers after the given amount of days have passed.
"""
import math
def infected(days):
    total_infected_computers = 1 # day - 0

    for day in range(1, days + 1):
        total_infected_computers *= 2

        if day%3 == 0:
            patched_computers = math.ceil(0.2*total_infected_computers)
        else:
            patched_computers = 0

        total_infected_computers -= patched_computers

    return total_infected_computers
print(infected(3))
print(infected(25))  # 5217638


"""
Tests

Passed: 1. infected(1) should return 2.
Passed: 2. infected(3) should return 6.
Passed: 3. infected(8) should return 152.
Passed: 4. infected(17) should return 39808.
Paased: 5. infected(25) should return 5217638.
"""
