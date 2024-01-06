#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int):  width of new rectangle.
            height (int): height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return current area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return current perimeter of rectangle"""
        if self.__height == 0 or self.width == 0:
            return (0)

        return (2 * (self.__height + self.__width))
