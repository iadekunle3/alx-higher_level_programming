#!/usr/bin/python3

"""This module is for 1-my_list"""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """print out the sorted list"""
        print(sorted(self))
