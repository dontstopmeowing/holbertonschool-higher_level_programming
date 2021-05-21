#!/usr/bin/python3
"""An empty class Rectangle"""


class Rectangle:
    """Defining a rectangle.
    Attributes:
        __size: size of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inits the Rectangle with its width and height."""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
                if i == self.__height - 1:
                    tmp += str(self.print_symbol) * self.__width
                else:
                    tmp += str(self.print_symbol) * self.__width + "\n"
        return tmp

    def __repr__(self):
        """Returns a representation of the rectangle for reproduction"""
        # return "Rettangolo({0}, {1})".format(self.base, self.altezza)
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    # __del__ is a destructor method which is called as soon as
    # all references of the object are deleted
    def __del__(self):
        """Deletes the entire rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
