#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for now in matrix:
        for noy in now:
            print("{:d}".format(noy), end=" " if noy != now[-1] else "")
        print()
