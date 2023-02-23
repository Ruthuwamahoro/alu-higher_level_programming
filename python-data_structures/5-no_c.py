#!/usr/bin/python3
def no_c(my_string):
    char = 'c','C'
    new_string = list(map(lambda x:x.replace(char, ''), my_string))
    return new_string
