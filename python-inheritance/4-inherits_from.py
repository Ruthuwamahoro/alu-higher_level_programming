#!/usr/bin/python3
"""function that return True if an object
is an instance of class that inherited"""


def is_kind_of_class(obj, a_class):
    """through implementationed"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
