#!/usr/bin/python3
''' module for append_after function '''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file, after each line
    containing a specific string'''
    with open(filename, 'r', encoding="UTF-8") as f:
        lines_list = []
        while True:
            line = f.readine()
            if line = "":
                break
            lines_list.append(line)
            if search_string in line:
                lines_list.append(new_string)
    with open(filename, 'w', encoding="UTF-8") as f:
        f.writelines(lines_list)
