#!/usr/bin/python3
def multiple_returns(sentence):
    original_tuple = ()
    if len(sentence) == 0:
        original_tuple = 0, "None"
    else:
        original_tuple = len(sentence), sentence[0]
    return original_tuple
