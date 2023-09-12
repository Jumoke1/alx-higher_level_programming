#!/usr/bin/python3
'''Define empty class BaseGeometry'''


class BaseGeometry:
    '''Represent basegeometry class'''

    def area(self):
        '''Not iplemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Representing integer validator

     Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
     '''
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise TypeError("{} must be greater than 0".format(name))
