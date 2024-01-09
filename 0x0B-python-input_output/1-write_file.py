#!/usr/bin/python3
"""Define a write function"""


def write_file(filename="", text=""):
    """write a string to a UTF8 text file

    Args:
        filename (str): The name of the file to write
        text (str): The text to write in the file
    Returns:
        the number of charater written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
