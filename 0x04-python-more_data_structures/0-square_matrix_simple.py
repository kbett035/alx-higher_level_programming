#!/usr/bin/python3
# Wyclife Kimutai <kimutaiwyclife6@gmail.com>
# 0-square_matrix_simple.py



def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
