#!/usr/bin/python3
def element_at(my_list, x):
    if x < 0:
        return(None)
    length = len(my_list)
    if x > length - 1:
        return(None)
    return(my_list[x])
