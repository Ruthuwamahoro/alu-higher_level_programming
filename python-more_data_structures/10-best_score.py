#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = list(a_dictionary.items())[0][1]
    for i,n in a_dictionary.items():
        if n > biggest.:
            biggest = n
    for i,n in a_dictionary.items():
        if n == biggest:
            return i
