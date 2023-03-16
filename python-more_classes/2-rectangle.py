#!/usr/bin/python3

"""we don't have to import any module just define rectangle"""


class Rectangle:
    """representation of rectangle class"""

    def __init__(self, width=o, height=0):
        """initialization of instance attribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieving value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value of width"""

        if not isinstance(value, int):
            return TypeError('width must be an integer')
        if value < 0:
            return ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """returning value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting value of height"""

        if not isinstance(value, int):
            return TypeError('height must be an integer')
        if value < 0:
            return ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculating area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculating perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
