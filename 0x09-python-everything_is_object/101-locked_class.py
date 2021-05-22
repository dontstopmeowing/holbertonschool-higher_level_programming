#!/usr/bin/python3
"""
Class that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called
"""


class LockedClass:
    """__slots__ for faster attribute access."""
    # Another purpose of __slots__ is to reduce the space in memory
    # that each object instance takes up.
    __slots__ = 'first_name'
