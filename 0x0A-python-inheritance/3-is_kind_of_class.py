#!/usr/bin/python3
"""Defineing class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checking if an object is an instance or inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        When  obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
