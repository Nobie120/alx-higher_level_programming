#!/usr/bin/python3
''' Module For Checking if an object is an intsance '''


def is_same_class(obj, a_class):
    '''Checks if an Object is an instance of
    a certain class
    Args:
        obj:The object
        a_class: the class

    Returns:
        True:if is an instance
        otherwise False
    '''
    return (isinstance(obj, a_class))
