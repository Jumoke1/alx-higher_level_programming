#!/usr/bin/python3
"""Defines an append function"""


def append_write(filename="", text=""):
    """Append a string at the end of the text file.

     Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters addedd
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
