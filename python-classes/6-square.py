#!/usr/bin/python3
"""module that defines square"""

class Square:
    """representation od square class"""
    def __init__(self, size=0, position=(0,0)):
        self.__size=size
        self.__position=position
    @property
    def size(self):
        """getting value of size"""
        self.__size=size
    @size.setter    
    def size(self,value):
        """to set value of size"""
        self.__size=value
        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if size < 0:
            return ValueError('size must be >= 0')
    @property
    def position(self):
        """getting value of position attribute"""
        return self.__position
    @position.setter
    def position(self,value):
        """setting value of position"""
        return self.__position=value
        if not isinstance(value, tuple) or len (value) != 2:
            return TypeError('position must be a tuple of 2 positive integers')
        if len ([n for n in value if isinstance(n, int) and n >= 0]) != 2:
            return TypeError('position must be a tuple of 2 positive integers')
    def area(self):
        """return the current square area"""
        return self.__size * self.__size
    def my_print(self):
        """print stdout the square with the character"""
        if self.__size == 0
            print()

        for n in range(self.__position[1]):
            print("")
        for v in range(0, self.__size):
            for m in range(0, self.__position[0]):
                print(" ",end="")
            for z in range(0,self.__size):
                print("#", end="")
                print("")   
