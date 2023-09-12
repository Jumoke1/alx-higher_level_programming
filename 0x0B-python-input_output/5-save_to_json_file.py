#!/usr/bin/python3
"""Defines an JSON file writting function"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
