#!/usr/bin/python3

"""module that defines a square """

class Square:
    """this is a square class"""
    def __init__(self, size=0):
        """initialization of instance attribute"""

        self.__size = size
        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if size < 0:
            return ValueError('size must be >= 0')
    


    @property
    def size(self):
        """getting value of size """
        return self.__size
    @size.setter
    def size(self, value):
        """setting value of size"""
        self.__size = value
        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if size < 0:
            return ValueError('size must be >= 0')
         


    def area(self):
        """calculating square area"""
        return (self.__size ** 2)

