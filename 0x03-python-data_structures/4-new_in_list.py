#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx == -1 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.copy()  # Create a copy of the original list
        new_list[idx] = element
        return new_list
