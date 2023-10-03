#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for c in str:
        print("{:c}".format(
            ord(c) if not islower(c) else ord(c) - 32),
            end="")
    print("")
