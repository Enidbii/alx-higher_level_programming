#!/usr/bin/python3
""" readfile function """


def read_file(filename=""):
    """ reads file and prints it out to stdout """
    filename = "UTF8"
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
