#!/usr/bin/python3
"""Defining locked class"""


class LockedClass:
    """
    This prevents the user from instantiating new LockedClass
    attributes for anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
