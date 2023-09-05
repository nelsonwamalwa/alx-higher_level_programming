#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Printing numbers from 1 to 100 separated by a  white space

    Multiples of three, prints Fizz instead of the given number
    Multiples of five, prints Buzz instead of the given number
    Multiples of three and five, printS FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
