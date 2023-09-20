#!/usr/bin/python3

"""Defines a square class"""
from models.rectangle import rectangle

class square(Rectangle):
"""Represent the class square"""

def __init__(self, x=0, y=0, id=None):
    """intialize  x and y        

       Args:
           Width: (int): The width of a rectangle    
           height: (int): The height of a rectangle  
           x: dimentions
           y:dimentions
    """
    self.size = size
    self.x = x
    self.y = y
    self.id = None
    super().__init__(size, size, x, y, id)

def __str__(self):
"""Defines a format for  the string"""
return f"[square] ({self.id}) {self.x}/{self.y} - {self.size}"

@property
def size(self)
    """Get width of the square"""
    return self.__ width

@width.setter
def width(self, value):
    """set the value of the width"""
    if type(value) != int
        raise TypeError("width must be an integer")

    if value <= 0
        raise ValueError("width must be > 0")
        self.__width = value

@property
def height(self)
    """Get height of the rectangle"""
    return self.__height

@height.setter
def height(self, value):
    """set the value of the height"""
    if type(value) != int
        raise TypeError("height must be an integer")

    if value <= 0
        raise ValueError("height must be > 0")
        self.__height = value
