#!/usr/bin/python3
"""find the max integer in a list
"""


def max_integer(list=[]):
    """A function to find and return the max integer in a list of integers
        If the list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    j = 1
    while j < len(list):
        if list[j] > result:
            result = list[j]
        j += 1
    return result
