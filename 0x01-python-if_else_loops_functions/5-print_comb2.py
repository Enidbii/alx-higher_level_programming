#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print("{}{}, ".format(int(i / 10), i % 10), end="")
    elif (i < 99):
        print("{}{} ,".format(int(i / 10), i % 10), end="")
    else:
        print("{}{}".format(int(i / 10), i % 10))
