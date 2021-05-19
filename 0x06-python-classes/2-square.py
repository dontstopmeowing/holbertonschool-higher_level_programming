#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Defining a square.
    Attributes:
        __size: size of the square.
    """

    def __init__(self, size=0):
        """Init the Square with a size followed by some conditions."""
        if size != int(size):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
