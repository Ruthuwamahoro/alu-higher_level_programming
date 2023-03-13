#!/usr/bin/python3
"""we are not allowed to import any module"""

class Square:
    """This is a class that represents Square class"""
    def __init(self,size=0):
        """initialization of class"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
    @property
    def size(self):
        """this method is going to returns the size of square"""
        return self.__size = size
    @size.setter
    def size(self,value):

        """this method is all about sise and value"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

        def area(self):
            """by calculating an area of square"""
            return (self.__size ** 2)

        
