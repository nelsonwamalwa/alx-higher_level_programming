#!/usr/bin/python3
"""Defining the rectangle class"""


class Rectangle:
    """Representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing the new Rectangle.

        Args:
            width (int): width and type of the new rectangle
            height (int):  height and type of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """setting the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is setting the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        self.__height = value
