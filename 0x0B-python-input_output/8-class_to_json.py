#!/usr/bin/python3
"""
    This file contains the function save_to_json_file
"""


def class_to_json(obj):
    """
        Returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
    """

    return(obj.__dict__)
