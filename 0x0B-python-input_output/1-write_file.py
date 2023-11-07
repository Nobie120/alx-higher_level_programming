#!/usr/bin/python3
''' Module for writing in a file '''


def write_file(filename="", text=""):
    '''writes into a file and overwrite the previous content
    Args:
        filename - name of file
        text - what to be writen into the file
    Returns:
        the number of characters written:
    '''
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text) 
