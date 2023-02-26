#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiply_ditc = dict(a_dictionary)
    for e, a in multiply_ditc.items():
        multiply_ditc[e] = a * 2
    return multiply_ditc
