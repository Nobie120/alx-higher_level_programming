#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as fn

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, fn.add(a, b)))
    print("{} - {} = {}".format(a, b, fn.sub(a, b)))
    print("{} * {} = {}".format(a, b, fn.mul(a, b)))
    print("{} / {} = {}".format(a, b, fn.div(a, b)))
