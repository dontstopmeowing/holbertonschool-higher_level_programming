#!/usr/bin/python3
"""
    This file contains the class Student
"""


class Student:
    """Class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        new = {}
        if attrs is None:
            return(self.__dict__)
        for i in attrs:
            try:
                new[i] = self.__dict__[i]
            except:
                pass
        return new

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for i in json:
            self.__dict__[i] = json[i]
