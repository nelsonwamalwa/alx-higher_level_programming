#!/usr/bin/python3
"""Defining  an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checking if an object is an inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
