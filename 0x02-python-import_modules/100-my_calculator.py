#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    lenght = len(argv)
    if lenght != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)

    from calculator_1 import add, sub, mul, div
    ops = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if ops == '+':
        print("{:d} + {:d} = {}".format(a, b, add(a, b)))
    elif ops == '-':
        print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
    elif ops == '*':
        print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
    elif ops == '/':
        print("{:d} / {:d} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
