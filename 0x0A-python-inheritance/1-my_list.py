#!/usr/bin/python3
"""Defines a list that inherits from class list"""


class MyList(list):
    """Implement the sorted print for buit in list class"""

    def print_sorted(self):
        """print a list in sorted ascending order"""
    print(sorted(self))
