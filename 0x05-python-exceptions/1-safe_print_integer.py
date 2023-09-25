#!/usr/bin/python3


def safe_print_integer(value):
    """Printing an integer with "{:d}".format().

    Args:
        value (int): Given integer to print.

    Returns:
        When TypeError or ValueError occurs - false.
        Otherwise - true.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
