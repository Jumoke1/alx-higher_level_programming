#!/usr/bin/python3
"""Defines a  rectangle class"""


class Rectangle(Base):
"""Represent the class rectangle"""

def __init__(self, width, height, x=0, y=0, id=None):
    """intialize a new width, height, x and y

       Args:
           Width: (int): The width of a rectangle
           height: (int): The height of a rectangle
           x: dimentions
           y:dimentions
    """
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)

@property
def width(self)
    """Get width of the rectangle"""
    return self.__width

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

@property
def x(self)
    """Get the value for x"""
    return self.__x

@x.setter
def x(self, value):
    """set the value of the y"""
    if type(value) != x
        raise TypeError("x must be an integer")

    if value <= 0
        raise ValueError("x must be >= 0")
        self.__x = x

@property
def y(self)
    """Get the value for x"""
    return self.__y

@x.setter
def x(self, value):
    """set the value of the y"""
    if type(value) != y
        raise TypeError("y must be an integer")

    if value <= 0
        raise ValueError("y must be >= 0")
        self.__y = y

def area(self):
    """area  of rectangle"""
    return (self.__width * self.__height)


def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
 
