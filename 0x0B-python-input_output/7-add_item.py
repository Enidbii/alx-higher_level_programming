#!/usr/bin/python3
""" add item to list """


from sys import argv
Save_to_json = __import__('5-save_to_json_file').Save_to_json
Load_from_json = __import__('6-load_from_json_file').Load_from_json


filename = 'add_item.json'
thi_list = []
try:
    thi_list = Load_from_json(filename)
except Exception:
    Save_to_json(thi_list, filename)

len_args = len(argv)


if len_args > 1:
    for i in range(1, len_args):
        thi_list.append(argv[i])

    Save_to_json(thi_list, filename)
