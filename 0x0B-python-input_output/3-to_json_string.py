#!/usr/bin/python3
"""Defines a string conversion to json function"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a sstring"""
    return json.dumps(my_obj)
