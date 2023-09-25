#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Printing an integer with "{:d}".format().

    If the ValueError message is caught, corresponding
    message is printed to standard error

    Args:
        The value (int): integer to print.

    Returns:
        When TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
