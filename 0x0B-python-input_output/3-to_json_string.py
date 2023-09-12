#!/usr/bin/python3
"""Defines JSONrepresentation of oblect(string"""


def to_json_string(my_obj):
    """Return json reprsentation"""
    json_string = json.dumps(my_obj)
    return json_string
