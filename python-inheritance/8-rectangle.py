#!/usr/bin/python3
"""module that defines a class Rectangle from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing Rectange from BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of new instances of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
