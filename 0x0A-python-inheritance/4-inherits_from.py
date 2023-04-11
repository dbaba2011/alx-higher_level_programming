#!/usr/bin/python3
""" one sub class of """


def inherits_from(obj, a_class):
    """ function that displays True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
