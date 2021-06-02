#!/usr/bin/python3
"""
    This file contains the function save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """
        Writes an Object to a text file, using a JSON representation
    """

    with open(filename, 'w', encoding='utf-8') as staroba:
        json.dump(my_obj, staroba)
