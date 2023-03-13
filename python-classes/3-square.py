#!/usr/bin/python3
"""we don't have to import any mpodule"""

class Square:
    """initialization of class"""
    if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        def area(self):
            """This method is going to return square of area"""
            return (self.__size ** 2)
