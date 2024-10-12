"""
Python Development II Assignment 3: Prime Factors
Geetha Ramesh

test_generate_prime_factors.py

Unit tests for the generate_prime_factors function.

This module contains test cases for validating the behavior of the
generate_prime_factors function, which generates a list of prime
factors for a given integer.
"""

import pytest
from prime import generate_prime_factors


def test_datatype_not_integer():
    """
    Test to check if generate_prime_factors() function
    raises a ValueError for any input that is not an integer.
    """
    with pytest.raises(ValueError):
        generate_prime_factors("number")
    with pytest.raises(ValueError):
        generate_prime_factors(2.4)
    with pytest.raises(ValueError):
        generate_prime_factors(True)


def test_with_input_one():
    """
    Test if generate_prime_factors() function returns an empty list []
    when argument passed is 1.
    """
    input_value = 1
    expected_result = []
    assert generate_prime_factors(input_value) == expected_result
