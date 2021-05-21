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

    def area(self):
        """Returns the div of heigh and width"""
        res = self.__height * self.__width
        return res

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        res = self.__width * 2 + self.__height * 2
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return res

    def __str__(self):
        """Returns a printable version of the rectangle"""
        tmp = ""
        if self.__width == 0 or self.__height == 0:
            return tmp
        else:
            for i in range(self.__height):
                tmp += "{:s}".format(self.__width * "#")
                if i is not self.__height - 1:
                    tmp += "\n"
        return tmp
