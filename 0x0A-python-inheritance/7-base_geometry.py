#!/usr/bin/python3
"""
This file contains an empty class
"""


class BaseGeometry():
    """
    BaseGeometry class that DOES...


    something :O
    """

    def area(self):
        """Method that has not been implemented yet :("""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value and raises either TypeError
        if value is NOT an integer
        otherwise ValueError provided
        the value passed through the method is NOT greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
