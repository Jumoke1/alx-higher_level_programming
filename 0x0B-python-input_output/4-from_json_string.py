#!/usr/bin/python3
"""Defines a JSON to object convertion function"""
import json


def from_json_string(my_str):
    """Returns the python object representation of a string"""
    return json.loads(my_str)
