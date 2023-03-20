#!/usr/bin/python3
"""function that return list of available attribute"""


def lookup(obj):
    """return list of available attribute"""
    list = []
    for n in dir(obj):
        list = list.append(n)
        return list
