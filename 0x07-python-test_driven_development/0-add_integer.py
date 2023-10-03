#!/usr/bin/python3
# 0-add_integer.py
"""Defining  an integer in the addition function."""


def add_integer(a, b=98):
    """Returning the integer addition of a and b.

    Float arguments are typecasted to ints before addition is raised

    Raises:
        TypeError: If either of a or b is a non-integer and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

