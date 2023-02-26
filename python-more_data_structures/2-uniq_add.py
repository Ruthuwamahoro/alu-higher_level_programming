#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = []
    unique_numbers = set(my_list)
    for num in unique_numbers:
        unique_integers.append(num)
    return sum(unique_integers)    
