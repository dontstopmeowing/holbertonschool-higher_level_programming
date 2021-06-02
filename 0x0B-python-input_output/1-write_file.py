#!/usr/bin/python3
"""
    This file contains the function write_file
"""


def write_file(filename="", text=""):
    """
        Writes and returns the number of chars written to a file.
    """

    with open(filename, 'w', encoding='utf-8') as staroba:
        return staroba.write(text)
