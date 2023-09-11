#!/usr/bin/python3
'''A class mylist that inherit from list'''


class MyList(list):
    '''Implements sorted printing for built-in class'''

    def print_sorted(self):
        '''Sorting in accending order'''
        sorted_lis = sorted(self)
        print(sorted_lis)
