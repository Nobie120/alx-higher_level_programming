#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by
"""


class Rectangle:
    """ Representation of a recyangle """
    def __init__(self, width=0, height=0):
        """ Initialization """
        self.__width = width
        self.__height = height

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
