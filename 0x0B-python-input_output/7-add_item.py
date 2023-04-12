#!/usr/bin/python3
""" add item to list """


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        My_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        My_list = []
    My_list.extend(sys.argv[1:])
    save_to_json_file(My_list, "add_item.json")
