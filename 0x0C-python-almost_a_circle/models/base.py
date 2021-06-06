#!/usr/bin/python3
"""This file contains the Base class"""


class Base:
    """
        My Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes the Base class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
