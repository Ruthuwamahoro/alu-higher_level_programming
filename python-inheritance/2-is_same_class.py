#!/usr/bin/python3
"""function that returns True if object
is an instance of class otherwise
false"""


def is_same_class(obj, a_class):
    """return true if obj is an instance 
    of a_class otherwise False"""
    if isinstance(a_class, obj):
        return True
    return False
