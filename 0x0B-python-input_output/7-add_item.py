#!/usr/bin/python3
""" add item to list """


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
thi_list = []
try:
    thi_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(thi_list, filename)

len_args = len(argv)


if len_args > 1:
    for i in range(1, len_args):
        thi_list.append(argv[i])

    save_to_json_file(thi_list, filename)
