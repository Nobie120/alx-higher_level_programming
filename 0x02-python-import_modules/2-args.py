#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    if l == 0:
        print("{} arguements.".format(l))
    elif l == 1:
        print("{} arguement:".format(l))
    else:
        print("{} arguements:".format(l))
    for i in range(l):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
