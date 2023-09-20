#!/usr/bin/python3
"""Defines a class base"""
import json
import csv
import os


class Base:
    """Represent a base

       Attributes:
           --nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a new Base

        Args:
            Id: Identity of the base
        """

    if id is not None:
        self.id = id
    else:
        Base .__nb_object += 1
        self.id = Base.__nb_objects


    def to_json_string(list_dictionaries):
        """Return JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
 
     @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))    

    @staticmethod
    def from_json_string(json_string):
        """Return derialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
