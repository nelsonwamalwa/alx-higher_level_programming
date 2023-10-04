#!/usr/bin/python3
"""Module 6-rectangle
Defining a Rectangle class
"""


class Rectangle:
    """Rectangle class identified by width and height

    Attributes:
        number_of_instances: The number of rectangle instances,
        incrementing with every instantitation,
        decrementing with every deletion
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing a Rectangle instance

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returning an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returning a string representation of a rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deleting a rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieving the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of a Rectangle instance

        Args:
            value: The value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height of a Rectangle instance

        Args:
            value: The value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculating the area of rectangle instance

        Returns:
            Area of the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculating the perimeter of a Rectangle instance

        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
