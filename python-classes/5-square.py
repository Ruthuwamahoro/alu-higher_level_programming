#!/usr/bin/python3
"""module that defines a square"""


class Square:
    """representation of square class"""

    def __init__(self, size=0):
        """initialization of attribute"""
        self.__size = size
        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if size < 0:
            return ValueError('size must be >= 0')

    @property
    def size(self):
        """getting value of size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting value"""
        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if size < 0:
            return ValueError('size must be >=0')
        self.__size = value

    def area(self):
        """return current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout with the character #"""
        if self.__size == 0:
            print()
        for n in range(self.__size):
            print("#" * self.__size)
