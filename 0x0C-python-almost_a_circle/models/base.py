#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model of an object.

    Attribute:
         __nb_objects (int): The number of instantiated Bases.
    
    """

    __nb_objects = 0

    def __init__(self, id=None): 
        """Initializes a new basse

        Args:
            id (int): the identity of the new Base.
        """
        if id is not None:
            self.id = id 

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

