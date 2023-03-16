#!/usr/bin/python3

"""We don't need to import any module just define rectangle"""


class Rectangle:
    """representation of rectangle as a class"""

    def __init__(self, width=0, height=0):
        """initialization of instance attribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/access and return value of attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width value"""
        
        if not isinstance(value, int):
            return TypeError('width must be an integer')
        if value < 0:
            return ValueError('width must be >= 0')
        self.__width = value
    @property
    def height(self):
        """retrieve value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        
        if not isinstance(value, int):
            return TypeError('height must be an integer')
        if value < 0:
            return ValueError('height must be >= 0')
         self.__height = value
