#!/usr/bin/python3
"""function that prints"""
def say_my_name(first_name, last_name=""):
    """print name
    args:
        first_name:must be a string
        last_name:must be a string
    Returns:
        TypeError if first_name is not a  string
        TypeError if last_name is not a string
    """        

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
