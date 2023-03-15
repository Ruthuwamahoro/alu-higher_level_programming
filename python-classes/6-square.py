#!/usr/bin/python3
"""module that defines square"""

class Square:
    """representation od square class"""
    def __init__(self, size=0, position=(0,0)):
        self.size=size
        self.position=position
    def __str__(self):
        self.my_print()
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
        if not isinstance(value, tuple) or len (value) != 2 or
        len([n for n in value if isinstance(n, int) and n >= 0]) != 2:
            return TypeError('position must be a tuple of 2 positive integers')
        
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
