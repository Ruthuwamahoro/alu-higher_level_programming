#!/usr/bin/python3
"""module that defines square"""

class Square:
    """representation od square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of attribute"""
        self.size=size
        self.position=position
    
    @property
    def size(self):
        """getting value of size"""
        return self.__size

    @size.setter    
    def size(self,value):
        """to set value of size"""
        self.__size=value
        if not isinstance(size, int):
            return TypeError('size must be an integer')
        if value < 0:
            return ValueError('size must be >= 0')
    @property
    def position(self):
        """getting value of position attribute"""
        return self.__position
    @position.setter
    def position(self,value):
        """setting value of position"""
        return self.__position=value
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
    def area(self):
        """return the current square area"""
        return self.__size * self.__size
    def my_print(self):
        """print # character"""
        if self.__size == 0:
            print("")
            return 
        [print("") for num in range(0, self.__position[1])]
        for num in range(0, self.__size):
            [print(" ", end="") for t in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")
