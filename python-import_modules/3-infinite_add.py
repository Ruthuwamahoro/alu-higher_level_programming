#!/usr/bin/python3
if __name__="__main__":
    from sys import argv
    num=0
    x=len(argv)
    for i in (1,x):
        num += int(argv[i])
    print("{:d}".format(num))    
