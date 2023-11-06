#!/usr/bin/python3
''' module for Mylist subclass '''


class MyList(list):
    ''' Mylist Class '''
    def print_sorted(self):
        ''' Prints a sorted list '''
        print(sorted(self))
