#!/usr/bin/python3
"""
This file contains the class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
