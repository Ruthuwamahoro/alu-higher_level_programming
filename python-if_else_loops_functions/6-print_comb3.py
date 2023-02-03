#!/usr/bin/python3
for i in range(0, 10):
    for w in range(i + 0, 10):
        if i == 8 and w == 9:
            print(f"{i}{w}")
        else:
            print(f"{i}{w}", end=", ")


