 #!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_items = sorted(a_dictionary.items())
    for key, value in sort_items:
        print("{}: {}".format(key, value))~
