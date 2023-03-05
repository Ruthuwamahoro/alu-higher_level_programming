#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    return[[matri * matri for matri in member] for member in matrix]    
