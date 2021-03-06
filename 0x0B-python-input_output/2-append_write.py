#!/usr/bin/python3
"""
    This file contains the function append_write
"""


def append_write(filename="", text=""):
    """
        Creates, write, append text on a file
        and returns the number of chars written to the file.
    """

    with open(filename, 'a+', encoding='utf-8') as staroba:
        return staroba.write(text)
