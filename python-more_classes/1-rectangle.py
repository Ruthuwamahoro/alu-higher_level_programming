#!/usr/bin/python3

"""We don't need to import any module just define rectangle"""


class Rectangle:
    """representation of rectangle as a class"""

    def __init__(self, width=0, height=0):
        """initialization of instance attribute"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get/access and return value of attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width value"""
        self.__width = value
        if not isinstance(width, int):
            return TypeError('width must be an integer')
        if width < 0:
            return ValueError('width must be >= 0')

    @property
    def height(self):
        """retrieve value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        self.__height = value
        if not isinstance(height, int):
            return TypeError('height must be an integer')
        if height < 0:
            return ValueError('height must be >= 0')
