#!/usr/bin/python3

for j in range(0, 10):
    for i in range(1, 10):
        if j >= i:
            continue
        elif j == 8 and i == 9:
            print("{}{}".format(j, i))
        else:
            print("{}{}, ".format(j, i), end="")
