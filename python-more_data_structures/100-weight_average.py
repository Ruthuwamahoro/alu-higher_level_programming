#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return 0
    return sum([n*m for (n, m) in my_list]) / sum([m for (n, m) in my_list])
