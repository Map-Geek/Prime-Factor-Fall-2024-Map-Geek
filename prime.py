"""
Python Development II Assignment 3: Prime Factors
Geetha Ramesh

prime.py

This module provides the `generate_prime_factors` function, which takes an integer input
and returns a list of its prime factors. It raises a ValueError if the input is not a valid
integer (including booleans and non-numeric types).

Functions:
    - generate_prime_factors(number: int) -> list:
        Generates a list of prime factors of the input integer.

Exceptions:
    - Raises ValueError for non-integer inputs, including booleans and non-numeric types.
"""

import math


def generate_prime_factors(number):
    """
    Generate a list of prime factors for a given integer.

    :param number: the integer for which to find prime factors
    :returns: a list of prime factors of the input integer
    :raises: ValueError if input is not integer.
    """

    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("The input value must be an integer")

    prime_factors = []  # Initialise an empty list to store prime factors
    divisor = 2  # Set divisor to 2 (the smallest prime number)

    # Repeatedly check if number is even (divisible by 2), add divisor 2 which is a prime factor
    # to the prime factors list, update the number until it is no longer divisible by 2
    while number % divisor == 0:
        prime_factors.append(divisor)
        number = number // divisor

    # Check for odd factors starting from 3 up to or equal to the value of
    # the square root of number
    # Increment divisor by 2 (to skip even numbers)
    divisor = 3
    while divisor <= math.isqrt(number):
        while number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        divisor += 2

    # If there is any number left greater than 1, it is also a prime factor so add it to the list
    if number > 1:
        prime_factors.append(number)
    return prime_factors
