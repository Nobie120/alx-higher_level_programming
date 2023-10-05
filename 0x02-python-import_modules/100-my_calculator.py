#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as fn
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        print("{} + {} = {}".format(a, b, fn.add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, fn.sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, fn.mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, fn.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
