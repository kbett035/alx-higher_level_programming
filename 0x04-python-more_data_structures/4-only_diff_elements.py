#!/usr/bin/python3
# 4-only_diff_elements.py
# Wyclife Kimutai <kimutaiwyclife6@gmail.com>


def only_diff_elements(set_1, set_2):
    """Returns sets of all elements present in only one set."""
    return (set_1 ^ set_2)
