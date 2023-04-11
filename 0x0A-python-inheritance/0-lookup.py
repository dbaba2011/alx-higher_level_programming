#!/usr/bin/python3
"""Define an object attribute search function."""


def lookup(obj):
    """Return a list of an object's present attributes."""
    return (dir(obj))
