#!/usr/bin/python3
"""we don't need to import any module just define rectangle"""

class Rectangle:
    """representation of frectangle class"""
    def __init__(self, width=o, height=0):
        """initialization of instance attribute"""
        self.__width=width
        self.__height=height

    @property
    def width(self):
        """retrieving value"""
        return self.__width
    @width.setter
    def width(self,value):
        """setting value of width"""
        self.__width=value
        if not isinstance(width, int):
            return TypeError('width must be an integer')
        if width < 0:
            return ValueError('width must be >= 0')

    @property
    def height(self):
        """returning value"""
        return self.__height
    @height.setter
    def height(self, value):
        """setting value of height"""
        self.__height=value
        if not isinstance(height, int):
            return TypeError('height must be an integer')
        if height < 0:
            return ValueError('height must be >= 0')
    def area(self):
        """calculating area of rectangle"""
        return self.__height * self.__width
    def perimeter(self):
        """calculating perimeter of rectangle"""
        perimeter=(self.__height + self.__width) * 2
      
        if width == 0 or height == 0 :
            perimeter == 0
        return perimeter
