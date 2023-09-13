#!/usr/bin/python3
"""Defines a class students"""


class Student:
    """Represent a students details"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student

        Args:
            first_name: The student firstname
            last_name: The student lastname
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives dictionary representation of a student"""
        return self.__dict__
