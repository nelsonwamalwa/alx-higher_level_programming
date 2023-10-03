#!/usr/bin/python3
# 2-matrix_divided.py
"""Defining  a matrices division function."""


def matrix_divided(matrix, div):
    """Dividing all elements of a matrix

    Args:
        matrix (list): list of lists of ints or floats
        div (int/float): The is a  divisor
    Raises:
        TypeError: The matrix contains non-numbers
        TypeError: The matrix contains rows of different sizes
        TypeError: The  div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        The new matrix representing the result of the division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("The matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("To each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

