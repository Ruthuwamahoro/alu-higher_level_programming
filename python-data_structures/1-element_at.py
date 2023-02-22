#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 3
def element_at(my_list, idx):
    if 0 <= idx :
        return my_list[idx]
    elif idx < len(my_list) :
        return my_list[idx]
    else:
        return None
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

        
