#!/usr/bin/python3
"""Defining a class"""

from models.base import Base

class Rectangle(Base):
    """representation of Rectangle clasa that inherits from base class"""
    def__init__(self, width, height, x=0, y=0, id=None):
        """initialization of attribute"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
    @property
    def return_width(self):
        """method that return the value of width"""
        self.__width
    @width.setter
    def set_value_width(self, value):
        """method that set value to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getting a value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getting value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting a value of x"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
