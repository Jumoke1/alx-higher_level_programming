#!/usr/bin/python3
"""Defines a function for addition"""


def add_integer(a, b=98):
    """Return the sum of two integer

       Float values are casted to integers before addition

       Raises:
          TypeError: if either of a  or b is not integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
