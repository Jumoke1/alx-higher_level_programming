#!/usr/bin/python3
"""Defines a python data structure """
import json


def from_json_string(my_str):
    """Returns an onj represented by json string"""
    return json.loads(my_str)
