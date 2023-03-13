#!/usr/bin/python3

""" we don't have to import any module"""


class Square:
    """Square is the product of a number multiplied by itself"""
    def __init__(self, size=0):

        """ initialization of square class"""
        if not isinstance(size, int):

            raise TypeError('size must be an integer')

        elif size < 0 :

            raise ValueError('size must be >= 0')

        self.__size = size
            
       







        

