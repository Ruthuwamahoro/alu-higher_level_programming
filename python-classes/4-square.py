#!/usr/bin/python3

"""module that defines a square """

class Square:
    """this is a square class"""
    def __init__(self, size=0):
        """initialization of instance attribute"""
        self._size=size

        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if size < 0:
            return ValueError('size must be >= 0')

    @property
    def size(self):
        """getting value of size """
        return self._size
    @size.setter
    def size(self, value):
        """setting value of size"""
        self._size=value
        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if size < 0:
            return ValueError('size must be >= 0')

    def area(self):
        """calculating square area"""
        return (self._size ** 2)
