#!/usr/bin/python3
"""Defining function that check object instance inheritance."""


def inherits_from(obj, a_class):
    """Through implementation
    checks whether object is an instance
    of class that inherited return True
    otherwise False"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

