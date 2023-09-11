#!/usr/bin/python3
'''A function that retrns true if obj is an instance of clas'''


def is_same_class(obj, a_class):
    '''Check if an obj is an instance of a class.

     Args:
         obj (any): The object
         a_class (type): The class to match thhe obj
     Return:
         if obj is exactly an instance return true
         Otherwise - False.
    '''
    if type(obj) == a_class:
        return True
    return False
