#!/usr/bin/python3
"""
This file contains a subclass and the print_sorted function:
"""


class MyList (list):
    """Class MyList that inherits from list."""

    def __init__(self):
        """Initializes the object of the class itself."""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list."""
        sortmepls = sorted(self)
        print(sortmepls)
