# -*- coding: utf-8 -*-
""" Collatz sequence challenge, posted at
https://www.reddit.com/r/dailyprogrammer/comments/6e08v6/20170529_challenge_317_easy_collatz_tag_system/."""

# authorship information
__author__ = 'Scott Crowe'
__email__ = 'sb.crowe@gmail.com'
__license__ = 'MIT'

# define challenge input
_input = ['aaa', 'aaaaaaa']

def collatz_sequence(initial_word, deletion_number = 2, production_rules = {'a': 'bc', 'b': 'a', 'c': 'aaa'}):
    """ Computes a collatz sequence, wherein the words are determined (until length < deletion numbers) by:
    1) deleting the first m (deletion number) symbols
    2) appending production word P(x) calculated using the first symbol x.
    2) appending production word P(x) calculated using the first symbol x.

    Args:
        initial_word (string): The starting word.
        deletion_number (int): The positive integer used to determine deletion and halting.
        production_rules (dict): Production rules associating symbols with production words.
    """
    word = initial_word
    sequence = [initial_word]
    while len(word) >= deletion_number:
        word = word[deletion_number:] + production_rules[word[0]]
        sequence.append(word)
    return sequence

for case in _input:
    print(collatz_sequence(case))