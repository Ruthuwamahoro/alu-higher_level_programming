#!/usr/bin/python3

"""we are not allowed to import any module so this module defines square"""


class Square:

    """This class is called square"""

    def __init__(self, size=0):
        """initialization of class attribute"""
        self._size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculation of square area"""
        return (self._size ** 2)

