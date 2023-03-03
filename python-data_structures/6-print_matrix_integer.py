#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for now in matrix:
        for noy in now:
            if noy != now[-1]:

                print("{:d}".format(noy), end=" ")
            else:
                print("")
        print()
