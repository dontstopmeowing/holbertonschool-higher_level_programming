#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Defining a square.
    Attributes:
        __size: size of the square.
    """

    def __init__(self, size=0):
        """Init the Square"""
        self.__size = size

    @property
    def size(self):
        """Returns the Square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets Square with a size subject to certain conditions."""
        if type(size) != int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """print in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
