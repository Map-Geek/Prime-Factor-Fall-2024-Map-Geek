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


def generate_prime_factors(number):
    """
    Generate a list of prime factors for a given integer.

    :param number: the integer for which to find prime factors
    :returns: a list of prime factors of the input integer
    :raises: ValueError if input is not integer.
    """
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("The input value must be an integer")

    if number == 1:
        return []
