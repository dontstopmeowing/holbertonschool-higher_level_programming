#!/usr/bin/python3
"""Function that prints a name"""


def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    elif size > 0:
        for i in range(size):
            print("#" * size)
