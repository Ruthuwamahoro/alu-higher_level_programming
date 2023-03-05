#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for n in range(x):
            print(my_list[n], end='')
            number += 1
    except:
        pass
    print()
    return number
