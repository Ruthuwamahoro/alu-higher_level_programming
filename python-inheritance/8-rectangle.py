#!/usr/bin/python3
"""module that defines a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representation of Rectangle from BaseGeometry"""

    def __init(self, width, height):
        """initialization of new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
