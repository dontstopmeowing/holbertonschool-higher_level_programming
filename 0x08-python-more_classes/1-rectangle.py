#!/usr/bin/python3
"""An empty class Rectangle"""


class Rectangle:
    """Defining a rectangle.
    Attributes:
        __size: size of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Inits the Rectangle with its width and height."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the private attribute width"""
        return self.__width

    @width.setter
    def width(self, n):
        """Setter for the private attribute width"""
        if n != int(n):
            raise TypeError("width must be an integer")
        elif n < 0:
            raise ValueError("width must be >= 0")
        self.__width = n

    @property
    def height(self):
        """Returns the private attribute height"""
        return self.__height

    @height.setter
    def height(self, n):
        """Setter for the private attribute height"""
        if n != int(n):
            raise TypeError("height must be an integer")
        elif n < 0:
            raise ValueError("height must be >= 0")
        self.__height = n
