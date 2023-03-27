#!/usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    rand_no = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            rand_no += 1
        except IndexError:
            print("Sorry, that index does not exist")
            break
    print()
    return rand_no
