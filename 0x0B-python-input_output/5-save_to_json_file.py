#!/usr/bin/python3
"""Defines an object using JSON representation"""


def save_to_json_file(my_obj, filename):
    """write an object to a text file

    Args:
        my_obj: The object to write
        filename: The name of the file
    """
    with open(filename, "w") as f:
        return json.dumps(my_obj, f)