#!/usr/bin/python3
# 9-multiple_by_2.py


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multipled by two."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
