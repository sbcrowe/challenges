# -*- coding: utf-8 -*-
""" Subset sum challenge, posted at
https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/. """

# authorship information
__author__ = 'Scott Crowe'
__email__ = 'sb.crowe@gmail.com'
__license__ = 'MIT'

import itertools as it

# define challenge input
_input = [[1, 2, 3], [-5, -3, -1, 2, 4, 6], [], [-1, 1], [-97364, -71561, -69336, 19675, 71561, 97863],
           [-53974, -39140, -36561, -23935, -15680, 0]]

_bonus_input = [
    [-83314, -82838, -80120, -63468, -62478, -59378, -56958, -50061, -34791, -32264, -21928, -14988, 23767, 24417,
     26403, 26511, 36399, 78055],
    [-92953, -91613, -89733, -50673, -16067, -9172, 8852, 30883, 46690, 46968, 56772, 58703, 59150, 78476, 84413, 90106,
     94777, 95148],
    [-94624, -86776, -85833, -80822, -71902, -54562, -38638, -26483, -20207, -1290, 12414, 12627, 19509, 30894, 32505,
     46825, 50321, 69294],
    [-83964, -81834, -78386, -70497, -69357, -61867, -49127, -47916, -38361, -35772, -29803, -15343, 6918, 19662, 44614,
     66049, 93789, 95405],
    [-68808, -58968, -45958, -36013, -32810, -28726, -13488, 3986, 26342, 29245, 30686, 47966, 58352, 68610, 74533,
     77939, 80520, 87195],
    [-97162, -95761, -94672, -87254, -57207, -22163, -20207, -1753, 11646, 13652, 14572, 30580, 52502, 64282, 74896,
     83730, 89889, 92200],
    [-93976, -93807, -64604, -59939, -44394, -36454, -34635, -16483, 267, 3245, 8031, 10622, 44815, 46829, 61689, 65756,
     69220, 70121],
    [-92474, -61685, -55348, -42019, -35902, -7815, -5579, 4490, 14778, 19399, 34202, 46624, 55800, 57719, 60260, 71511,
     75665, 82754],
    [-85029, -84549, -82646, -80493, -73373, -57478, -56711, -42456, -38923, -29277, -3685, -3164, 26863, 29890, 37187,
     46607, 69300, 84808],
    [-87565, -71009, -49312, -47554, -27197, 905, 2839, 8657, 14622, 32217, 35567, 38470, 46885, 59236, 64704, 82944,
     86902, 90487]]


def subset_sum(sequence):
    """ Determine if there are two integers in the list that add to 0, or if 0 appears in the list. Solution is
    inefficient.

    Args:
        sequence (list): The sequence of numbers.
    """
    for number in sequence:
        if -number in sequence:
            return True
    return False


def bonus_challenge(sequence):
    """ Determine if there is a subset of the sequence for which the sum is 0. Solution is really inefficient.

    Args:
        sequence (list): The sequence of numbers.
    """
    for combination_size in range(1,len(sequence),1):
        combinations = it.combinations(sequence, combination_size)
        for combination in combinations:
            if sum(combination) is 0:
                return True
    return False

# run the code
for case in _input:
    print(subset_sum(case))
for case in _bonus_input:
    print(bonus_challenge(case))