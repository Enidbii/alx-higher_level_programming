#!/usr/bin/python3
for x in reversed(range(65, 91)):
    if x % 2 == 0:
        x = x + 32
    print("{}".format(chr(x)), end="")
