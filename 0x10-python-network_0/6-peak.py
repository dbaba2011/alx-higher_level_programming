#!/usr/bin/python3
"""This module contains a function that returns a peak in an unsorted list"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    middle_num = int(size / 2)
    peak_num = list_of_integers[middle_num]
    if peak_num > list_of_integers[middle_num - 1] and peak > list_of_integers[middle_num + 1]:
        return peak_num
    elif peak_num < list_of_integers[middle_num - 1]:
        return find_peak(list_of_integers[:middle_num])
    else:
        return find_peak(list_of_integers[middle_num + 1:])
