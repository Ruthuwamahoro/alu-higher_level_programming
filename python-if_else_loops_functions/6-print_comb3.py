#!/usr/bin/python3
for x in range(0,10):
    for z in range(1, 10):
        if x >= z:
            continue
        elif x == 8 and z == 9:
            print("{}{}")
        else:
            print("{}{}".format(x,z), end=", ")



