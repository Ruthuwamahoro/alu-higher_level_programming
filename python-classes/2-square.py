class Square:
    """Square is the product of a number multiplied by itself"""
    def __init__(self, size=0):
        """initialization of class"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
