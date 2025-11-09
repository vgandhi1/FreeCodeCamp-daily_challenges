"""
Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
"""
def nth_prime(n):
    if n <= 0 :
        return "Incorrect number"

    if n == 1:
        return 2

    digit = 3

    prime_list = [2]
    while len(prime_list) < n:
        is_prime = True
        
        y = round(digit**0.5) 

        for div in range(3, y+1, 2):
            if digit%div == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(digit)
                

        digit += 2
         
    return prime_list[n-1]

print(nth_prime(5))


"""
Tests
Passed:1. nth_prime(5) should return 11.
Passed:2. nth_prime(10) should return 29.
Passed:3. nth_prime(16) should return 53.
Passed:4. nth_prime(99) should return 523.
Passed:5. nth_prime(1000) should return 7919.
"""

from math import isqrt

def nth_prime(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 2

    primes = [2]
    candidate = 3

    while len(primes) < n:
        limit = isqrt(candidate)
        is_p = True
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0:
                is_p = False
                break

        if is_p:
            primes.append(candidate)

        candidate += 2  # only odd numbers

    return primes[-1]
