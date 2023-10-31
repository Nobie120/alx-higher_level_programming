#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by
"""


class Rectangle:
    """ Representation of a recyangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialization """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ a getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ returns represenation of the rectanfle """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """ return a string to be able to recreate a new instance """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message for ecery deletion of an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest Rectangle
        Args:
            rect_1:the 1st rectangle
            rect_2:The 2nd rectangle
        Raises:
            TypeError:If not an instance of the rectangle class
        Returns:
            The larger rectangle(larger area)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Insatntiates a new square
        Args:
            size:the measurement of the new square
        Returns:
            new Rectangle instance with width == height == size
        """
        return cls(size, size)
