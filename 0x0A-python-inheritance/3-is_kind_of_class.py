#!/usr/bin/python3
''' Module to see if an object is instance '''


def is_kind_of_class(obj, a_class):
    ''' returns True if the object is an instance of,
    or if the object is an instance of a class that inherited a class
    Args:
        object(obj) and class(a_class)
    Returns:
        True or False regarding the conditions
    '''
    return (isinstance(obj, a_class))
