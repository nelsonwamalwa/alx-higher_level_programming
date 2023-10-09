#!/usr/bin/python3
"""Defining class-checking function."""


def is_same_class(obj, a_class):
    """Checking if an object is exactly an instance of a given class.

    Args:
        obj (any): The given  object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        when  obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
