#!/usr/bin/python3
"""This file contains the Base class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Writes the JSON string representation of list_objs to a file.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
