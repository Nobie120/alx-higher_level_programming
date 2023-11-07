#!/usr/bin/python3
''' Module for serialization '''


import json


def to_json_string(my_obj):
    '''changes an object into its JSON strings
    Args:
        obj - the object
    '''
    return json.dumps(obj)
