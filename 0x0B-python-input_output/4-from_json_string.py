#!/usr/bin/python3
''' Module for deserilization '''


import json


def from_json_string(my_str):
    '''function that returns an object from json
    representation
    Args:
        my_str - the object to be deserilized
    '''
    return json.loads(my_str)
