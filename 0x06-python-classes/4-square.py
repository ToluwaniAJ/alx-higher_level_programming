#!/usr/bin/python3

"""
1. Square with size validation
    Contains a Square class that defines a square which accepts
    a size at instantiation and provides a function for calculating
    it's area.
"""


class Square:
    """
    A square class that accepts a size
    """

    def __init__(self, size=0):
        """
        initialize class with size
        """
        self.size = size

    @property
    def size(self):
        """
        get size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size ** 2
