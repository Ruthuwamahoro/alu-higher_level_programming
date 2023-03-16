#!/usr/bin/python3

"""we don't need to import any module just defines a Rectangle class."""



class Rectangle:


    """Representation of  a rectangle as a class."""

    def __init__(self, width=0, height=0):
        """Initialization of new attribute"""
        self.width = width
        self.height = height


    @property
    def width(self):
        """retrieve value of  the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value of width of rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve values of  the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """setting value of height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return and calculate the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return and calculate perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))    
