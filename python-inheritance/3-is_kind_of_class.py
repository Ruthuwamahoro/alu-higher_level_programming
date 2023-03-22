#!/usr/bin/python3
"""function that return True if an object
is an instance of class that inherited from"""


def is_kind_of_class(obj, a_class):
    """through implementation
    Args:
        obj(any):object to check
        a_class:type of class to match
    Returns:
        True if obj is an instance
        otherwise false
        """
    if isinstance(obj, a_class):
        return True
    return False
