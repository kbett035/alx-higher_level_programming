#!/usr/bin/python3
# 100-safe_print_integer_err.py
# Wyclife Kimutai <kimutaiwyclife6@gmail.com

import sys


def safe_print_integer_err(value):
    """This Prints an integer with "{:d}".format().
    If a ValueError message is found, a corresponding
    message is printed to standard error.
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
