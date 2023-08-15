#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxInt = my_list[0]
    for j in my_list:
        if j > maxInt:
            maxInt = j
    return maxInt
