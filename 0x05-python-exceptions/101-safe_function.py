#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executing a function safely

    Args:
        fct: The function to execute
        args: Arguments for a given function.

    Returns:
        When error occurs - None.
        Otherwise - result of the called function
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
