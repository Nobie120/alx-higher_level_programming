#!/usr.bin/python3
''' Module for reading and writing files '''


def read_file(filename=""):
    '''reads a file and prints it to stdout
    Args:
        Filename-name of file
    '''
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
