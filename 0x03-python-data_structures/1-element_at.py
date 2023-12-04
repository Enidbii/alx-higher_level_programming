#!/usr/bin/python3
def element_at(my_list, x):
    length = len(my_list)
    if x < 0 || x > length - 1:
        return None
    return(my_list[x])
