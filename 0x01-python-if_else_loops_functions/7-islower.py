#!/usr/bin/python3
def islowe(c):
    ascii_num = ord(c)
    if ascii_num >= 97 and ascii_num <= 122:
        return True
    return False
