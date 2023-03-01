#!/usr/bin/python3
def safe_print_division(a, b):
    numb = 1
    try:
        numb = a / b
    except:
        numb = None
    finally:
        print("Inside result:{}".format(numb))
        return numb
