#!/usr/bin/python3

"""we don't have to import any module just define rectangle"""


class Rectangle:
    """representation of rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=o, height=0):
        """initialization of instance attribute"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """print rectangle with character"""
        total = ""
        if self.__height == 0 or self.width == 0:
            return total
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i is not self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        """return the string presentation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    @property
    def width(self):
        """retrieving value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value of width"""

        if not isinstance(value, int):
            return TypeError('width must be an integer')
        if value < 0:
            return ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """returning value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting value of height"""

        if not isinstance(value, int):
            return TypeError('height must be an integer')
        if value < 0:
            return ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculating area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculating perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2