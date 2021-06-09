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

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the JSON string representation of list_objs to a file.
        """
        content = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            content = []
            for i in list_objs:
                content.append(cls.to_dictionary(i))

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) < 1:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """
            Returns a list of instances.
        """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                content = cls.from_json_string(file.read())
                new = []
                for i in content:
                    new.append(cls.create(**i))
                return new
        except FileNotFoundError:
            return []
