#!/usr/bin/python3
''' module for 'class_to_json' function '''


def class_to_json(obj):
    ''' returns serializable objects '''
    return obj.__dict__
