#!/usr/bin/python3
""" load from json file function """


import json


def load_from_json_file(filename):
    """ creates an obj from a json file """
    with open(filename, "w", encoding="utf-8") as f:
        json.loads(f, filename)
