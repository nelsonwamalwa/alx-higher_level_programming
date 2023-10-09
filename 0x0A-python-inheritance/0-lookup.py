#!/usr/bin/python3
"""Defining an object attribute lookup function."""


def lookup(obj):
    """Returning a list of an object's available attributes."""
    return (dir(obj))
