#!/usr/bin/python3

if "--name--" == "--main--":
    import sys
    from variable_load_5 import a

    argv = len(sys.argv) - 1
    a = argv
    print("{} = {}".format(a, a))
