#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
    """Printing the last digits of a number and return"""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
