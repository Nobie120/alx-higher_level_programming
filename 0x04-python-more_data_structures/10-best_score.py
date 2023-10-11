#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxint = 0
    maxkey = None
    for key,value in a_dictionary.items():
        if value > maxint:
            maxint = value
            maxkey = key
    return maxkey
