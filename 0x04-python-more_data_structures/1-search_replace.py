#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_l = my_list[:]
    for i in range(len(my_list)):
        if new_l[i] == search:
            new_l[i] = replace
    return new_l
