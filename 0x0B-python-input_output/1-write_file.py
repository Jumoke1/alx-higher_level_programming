#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """write a string to utf8 text

    Args:
        filename (str): The name of the file to write.
        text (str): the text to write to the file.
    Returns:
        Returns no of character.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
