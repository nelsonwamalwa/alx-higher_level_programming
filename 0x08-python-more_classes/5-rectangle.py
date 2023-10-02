#!/usr/bin/python3
"""Defining rectangle class."""


class Rectangle:
    """Representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the width of the Rectangle."""
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

    def __str__(self):
        """Returning the printable representation of the Rectangle.

        Representing the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returning string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Printing message for every deletion of a Rectangle."""
        print("Bye rectangle. . . ")