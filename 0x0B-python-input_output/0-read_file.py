#!/usr/bin/python3
""" readfile function """


def read_file(filename=""):
    """ reads file and prints it out to stdout """
    with open("filename", 'r', encoding="utf-8") as f:
        read_data = f.read(size)

    print(read_data)
