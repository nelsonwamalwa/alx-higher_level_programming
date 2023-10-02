#!/usr/bin/python3
"""Defining the Rectangle class."""


class Rectangle:
    """Representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Setting the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Setting the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        self.__height = value

    def area(self):
        """Returning the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returning the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))