#!/usr/bin/python3
"""Module 9-rectangle
Defining a rectangle class.
"""


class Rectangle:
    """The rectangle class defined by width and height.

    Attributes:
        number_of_instances: The number of Rectangle instances,
        increments with every instantitation,
        decrements with every deletion
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing a rectangle instance.

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
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returning a string representation of a Rectangle instance
        that is able to recreate new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deleting a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieving the width of a Rectangle instance."""
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
        """Setting the height of a rectangle instance

        Args:
            value: The value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculating the area of a rectangle instance

        Returns:
            The area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculating the perimeter of a Rectangle instance

        Returns:
            The Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds biggest Rectangle based on the area

        Args:
            rect_1: The rectangle instance
            rect_2: The rectangle instance different from rect_1

        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creating a new rectangle instance with width == height == size

        Args:
            size: The size to set the new rectangle to

        Returns:
            New Rectangle instance
        """
        return cls(size, size)
