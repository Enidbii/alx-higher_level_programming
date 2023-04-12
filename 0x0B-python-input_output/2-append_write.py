#!/usr/bin/python3
""" append_write function """


def append_write(filename="", text=""):
    """ appends string to text file and returns no of characters """
    with open(filename, "a", encoding="utf-8") as text_file:
        append_text = text_file.write(text)
        return append_text
