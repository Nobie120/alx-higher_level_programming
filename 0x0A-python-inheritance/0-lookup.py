#!/usr/bin/python3


def lookup(obj):
    """returns the list
    of available attributes and methods of an object

    Args:
        obj:The object

    Returns:
        a list of attributes
    """
    return dir(obj)
