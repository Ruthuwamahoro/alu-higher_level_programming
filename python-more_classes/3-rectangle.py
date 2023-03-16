#!/usr/bin/python3

"""we don't need to import any module just defines a Rectangle class."""


class Rectangle:
    """Representation of a rectangle as a class"""

    def __init__(self, width=0, height=0):
        """Initialization of a new attribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returning value of width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """setting new value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returning the value of the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """setting new value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculating and returning  the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculating perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return string representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        tot = []
        for n in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if n != self.__height - 1:
                tot.append("\n")
        return ("".join(tot))     

