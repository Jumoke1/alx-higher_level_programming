#!/usr/bin/python3
"""Defines a function that read a text file"""


def read_file(filename=""):
    """Prints the contents of a UTF txt file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
