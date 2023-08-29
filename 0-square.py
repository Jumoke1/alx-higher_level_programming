#!/usr/bin/python3

class Square:
    """
    Class Square that defines a square.
    """

    def __init__(self, length):
        """
        Initialize the square with a given length.

        Args:
            length (float): The length of the sides of the square.
        """
        self.length = length

    def define_square(self, size):
        """
        Define the size of the square.

        Args:
            size (float): The size to be set for the square.
        """
        self.length = size

