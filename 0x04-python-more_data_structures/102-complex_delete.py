#!/usr/bin/python3
# Wyclife Kimutai <kimutaiwyclife6@gmail.com>
# 102-complex_delete.py



def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary"""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
