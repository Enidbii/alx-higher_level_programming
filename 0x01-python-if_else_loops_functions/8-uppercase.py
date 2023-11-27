#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        upper = str[c]
        if ord(str[c]) > 96 and ord(str[c]) < 123:
            upper = chr(ord(str[c]) - 32)
        print("{}".format(upper), end="")
    print()
