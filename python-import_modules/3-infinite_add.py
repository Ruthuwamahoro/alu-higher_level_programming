#!/usr/bin/python3
if __name__=="__main__":
    import sys
    
    x=len(sys.argv)
    num=0
    for i in (1,x):
        num += int(sys.argv[i])
    print("{:d}".format(num))
