#!/usr/bin/python3
"""defining a function that prints a square with character"""


def print_square(size):
    """Print a square with the character.
    Args:
        size:is integer and length of square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        [print("#", end="") for n in range(size)]
        print("")
