#!/usr/bin/python3
# Wyclife Kimutai <kimutaiwyclife6@gmail.com>
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """Prints dictionary by ordered keys"""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
