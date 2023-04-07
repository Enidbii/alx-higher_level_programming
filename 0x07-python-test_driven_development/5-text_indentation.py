#!/usr/bion/python3
""" text indentation module """


def text_indentation(text):
    """
        indents text after ./? and :

        Args:
            text: given text
    """
    text_to_split = list()
    splitted_text = list()
    letters_in_text = list()

    if type(text) is not str:
        raise TypeError("text must be a string")

    for word in text:
        letters_in_text.append(word)
        if word in ['.', '?', ':']:
            text_to_split.append(''.join(letters_in_text))
            letters_in_text.clear()

    if letters_in_text:
        text_to_split.append("".join(letters_in_text))
    letters_in_text.clear()

    for sentence in text_to_split:
        splitted_text.append(sentence.strip(' '))
    text_to_split.clear()

    for word in splitted_text[-1]:
        if word in ['.', '?', ':']:
            print("\n\n".join(splitted_text))
            print()
            return

    print("\n\n".join(splitted_text), end='')
