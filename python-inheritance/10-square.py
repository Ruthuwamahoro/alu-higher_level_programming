#!/usr/bin/python3
"""Module that defines a Rectangle base of Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a square as class."""

    def __init__(self, size):
        """Initialization of new instances of square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
