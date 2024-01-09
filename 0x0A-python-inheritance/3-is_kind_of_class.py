#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """checks if an onject is a n instance of an inherited class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if the obj is an instnce of an inherited class
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
