#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b):
    """Returns the addition of two integers"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return a + b
