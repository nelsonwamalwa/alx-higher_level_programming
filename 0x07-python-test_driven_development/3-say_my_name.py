#!/usr/bin/python3
# 3-say_my_name.py
"""Defining a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Printing a name.

    Args:
        first_name (str): A first name to print
        last_name (str): The last name to print
    Raises:
        TypeError: either of first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("The first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("The last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
