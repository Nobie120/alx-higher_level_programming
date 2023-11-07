#!/usr/bin/python3
''' Module for appending content to a file '''


def append_write(filename="", text=""):
    ''' Appends content to a file
    Args:
        filename - name of the file
        text - text to be appended
    '''
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
