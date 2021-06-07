#!/usr/bin/python3
"""
Contains the "Square" class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """My class square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square."""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter of size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size."""
        self.width = value
        self.height = value

    def __str__(self):
        """
            Returns the following format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
            Assigns an argument to the following attributes
            id, size, x, y.
        """
        keys = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)
