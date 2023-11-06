#!/usr/bin/python3
''' module for checking if an object is of inherited class '''


def inherits_from(obj, a_class):
    ''' checks if an object is an instance of a class that
    inherits from the specified class
    Args:
        The specified class(a_class) objec(obj)

    Returns:
        True if it is otherwise False
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
