#!/usr/bin/python3


"""
holds a class that defines a retangle
"""


'''Defines a Rectangle class.'''


class Rectangle:
    """
    defines a rectangle class
    """

    def __init__(self, width=0, height=0):

        """
        initialize a new instance of a rectangle
        """

        '''Initialize a new Rectangle,
        Args:
        width(int): width of the rectangle,
        height(int): height of the rectangle'''

        self.height = height
        self.width = width

    @property
    def width(self):
        """
        return the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        return the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
