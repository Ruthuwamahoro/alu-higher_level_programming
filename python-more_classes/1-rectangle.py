#!/usr/bin/python3

"""we don't need to import any modulie just Defines a Rectangle class."""


class Rectangle:
    """Representation of  rectangle as aclass"""

    def __init__(self, width=0, height=0):
        """Initialization of new instance attrubute""" 
        self.width = width
        self.height = height

    @property
    def width(self):
        """setting value of the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting value of height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
