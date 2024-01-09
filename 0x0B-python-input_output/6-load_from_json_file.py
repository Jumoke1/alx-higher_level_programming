#!/usr/bin/python3
"""Defines a json file read function"""
import json


def load_from_json_file(filename):
    """create a python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
