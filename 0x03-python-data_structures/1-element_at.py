#!/usr/bin/python3

def element_at(my_list, idx):
        if idx == -1:
            return "none"
        elif idx >= len(my_list):
            return "none"
        else:
	    return my_list[idx]
