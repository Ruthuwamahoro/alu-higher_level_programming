#!/usr/bin/python3
"""function that return True if an object
is an instance of class that inherited
directly or indirectly from
specific class"""


def is_kind_of_class(obj, a_class):
    """through implementation
    Args:
        obj(any):object to check
        a_class:type of class to match
    Returns:
        True if obj is an instanceof class
        inherited directly or directly
        """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
