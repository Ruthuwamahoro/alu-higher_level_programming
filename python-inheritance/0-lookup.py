#!/usr/bin/python3
"""function that return list of available attribute"""


def lookup(obj):
    """return list of available attribute"""
    return dir(obj)
