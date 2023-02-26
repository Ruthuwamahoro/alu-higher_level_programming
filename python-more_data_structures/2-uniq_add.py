#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = list()
    for inte in my_list:
        if inte not in unique_integers:
            unique_integers.append(inte)
    return sum(unique_integers)
