#!/usr/bin/python3
''' Module for lookup function '''


def lookup(obj):
    '''returns the list
    of available attributes and methods of an object
    Args:
        obj:The object

    Returns:
        list: lists of attributes
    '''
    return dir(obj)
