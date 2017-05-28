# -*- coding: utf-8 -*-
""" Concatenated integer challenge, posted at
https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/."""

# authorship information
__author__ = 'Scott Crowe'
__email__ = 'sb.crowe@gmail.com'
__license__ = 'MIT'

import itertools as it

# define challenge input
_input = ['79 82 34 83 69',
          '420 34 19 71 341',
          '17 32 91 7 46']


def concatenated_integers(sequence):
    """ Determines the smallest and largest values that can be obtained by concatenation of integers in sequence.
    Reportedly a question asked in Microsoft interviews. (This is a poor solution - permutations are inefficient.

    Args:
        sequence: The sequence of numbers.
    """
    #numbers = [int(x) for x in sequence.split()]
    numbers = sequence.split()
    permutations = list(it.permutations(numbers))
    concatenates = []
    for permutation in permutations:
        concatenate = ''.join(permutation)
        if not concatenate.startswith('0'):
            concatenates.append(''.join(permutation))
    concatenates = [int(x) for x in concatenates]
    return str(min(concatenates)) + ' ' + str(max(concatenates))

# run the code
for case in _input:
    print(concatenated_integers(case))