#!/usr/bin/python3

def element_at(my_list, idx):
    for index in my_list:
        if idx == -1:
            return "none"
        elif idx >= len(my_list):
            return "none"
        else:
            return my_list[idx]
