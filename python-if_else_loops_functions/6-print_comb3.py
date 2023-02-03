#!/usr/bin/python3

for i in range(0, 10):
    for w in range(i + 1, 10):
        if i == 8 and w == 9:
            print("{}{}".format(i, w))
        else:
            print("{}{}".format(i, w), end=", ")


