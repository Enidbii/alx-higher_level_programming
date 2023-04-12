#!/usr/bin/python3
""" save to json file function """


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using json repr """
    x = json.dumps(my_obj)
    filename = ""
    with open(filename, "w", encoding="utf-8") as file_txt:
        written = file_txt.write(x)
