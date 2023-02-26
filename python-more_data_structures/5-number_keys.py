#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_keys = list(a_dictionary.keys())
    my_keys.sort()
    sorted_dict = {n:a_dictionary[n] for n in my_keys}
    print(sorted_dict)

