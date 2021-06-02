#!/usr/bin/python3
"""
    This file contains the function read_file
"""


def read_file(filename=""):
    """
        Open and reads UTF-8 files
        based on the filename passed
        through the function.
    """
    with open(filename, 'r', encoding='utf-8') as staroba:
        print(staroba.read(), end="")
