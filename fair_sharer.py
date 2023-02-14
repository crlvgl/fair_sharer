# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:38:18 2023

@author: vogel
"""


def fair_sharer(values, num_iterations=1, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """

    temp = values
    values_new = []

    for _ in range(num_iterations):

        i_valn = temp.index(max(temp))

        if 1 <= 2 * share:
            break

        if i_valn == len(temp)-1:
            temp[0] += temp[i_valn]*share
        elif i_valn < len(temp)-1:
            temp[i_valn+1] += temp[i_valn]*share

        temp[i_valn-1] += temp[i_valn]*share
        temp[i_valn] = temp[i_valn]*(1 - 2 * share)

    for n in temp:
        values_new.append(float(n))

    return values_new
