#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers = 0
    for y in range(x):
        try:
            integer = my_list[y]
            print("{:d}".format(integer),end='')
            integers = integers + 1
        except(ValueError,TypeError):
            continue
    print()
    return integers
