#!/usr/bin/python3

"""module of define square"""


class Square:
    """defining square class"""

    def __init__(self, size=0):
        """Initializing instance attribute"""

        self.size = size

    @property
    def size(self):
        """Getting value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculating current area of the square."""
        return self.__size * self.__size
