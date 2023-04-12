#!/usr/bin/python3
""" write file function """


def write_file(filename="", text=""):
    """ writes string to a txt file and returns writen chars """
    with open(filename, "w", encoding="utf-8") as text_file:
        write_text = text_file.write(text)
        return (write_text)
