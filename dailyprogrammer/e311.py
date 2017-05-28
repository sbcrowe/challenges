# -*- coding: utf-8 -*-
""" Jolly Jumper challenge, posted at
https://www.reddit.com/r/dailyprogrammer/comments/65vgkh/20170417_challenge_311_easy_jolly_jumper/. """

# authorship information
__author__ = 'Scott Crowe'
__email__ = 'sb.crowe@gmail.com'
__license__ = 'MIT'

# define challenge input
_input = ['4 1 4 2 3',
          '5 1 4 2 -1 6',
          '4 19 22 24 21',
          '4 19 22 24 25',
          '4 2 -1 0 2']


def jolly_jumper(sequence):
    """ Determine if sequence of n > 0 integers is a 'jolly jumper' (with absolute values of differences between
    successive elements taking on all possible values 1 through n-1).

    Args:
        sequence: The sequence of numbers, preceded by a count (e.g. '4 1 4 2 3').
    """
    numbers = [int(x) for x in sequence.split()][1:]
    exp_diff = list(range(1, len(numbers), 1))
    diff = []
    for index in range(len(numbers) - 1):
        diff.append(abs(numbers[index + 1] - numbers[index]))
    if sorted(diff) == exp_diff:
        print(sequence + ' JOLLY')
    else:
        print(sequence + ' NOT JOLLY')


# run the code
for case in _input:
    jolly_jumper(case)
