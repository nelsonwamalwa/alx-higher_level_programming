#!/usr/bin/python3

def safe_print_division(a, b):
    """This returns the division of a by b"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
