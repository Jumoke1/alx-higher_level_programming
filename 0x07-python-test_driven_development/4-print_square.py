#!/usr/bin/python3
"""Defines a function that prints a square"""


def def print_square(size):
    """Print a square with # character.

    Args:
        size: size of square
        
    Raises:
       TypeError: if size is not an integer
       ValueError: if size is < 0
       TypeError: if size is not a float and less than 0
     """
    
     if not isinstance(size, int):
        raise TypeError("size must be an integer")
     if size < 0:
        raise ValueError("size must be >= 0")
     if not isinstance(size, float)
        raise TypeError("size must be an integer")
    
     for i in range(size):
         [print("#", end="") for j in range(size)]
         print("")
