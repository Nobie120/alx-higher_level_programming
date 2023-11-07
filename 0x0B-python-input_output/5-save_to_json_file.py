#!/usr/bin/python3
''' module for writing an Object to a file, using a JSON '''


import json


def save_to_json_file(my_obj, filename):
    '''write an object to a file in json representation
    Args:
        my_obj - the object
        filename -name of the file to be written on
    '''
    with open(filename, 'w', encoding="UTF-8"):
        json.dump(my_obj, filename)
