#!/usr/bin/python3

"""This module is for 2-is_same_class"""


def is_same_class(obj, a_class):
    """
    To check if the object is exactly an instance of the specified class
    Returns True if the object is exactly an instance of the specified class
    Returns False otherwise
    """
    return type(obj) is a_class
