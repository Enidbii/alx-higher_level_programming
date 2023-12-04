#!/usr/bin/python3
def element_at(my_list, x):
    if x < 0:
        return my_list
    length = len(my_list)
    if x > length - 1:
        return my_list
    return(my_list[x])
