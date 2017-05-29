# -*- coding: utf-8 -*-
""" Collatz conjecture program, described at https://github.com/karan/Projects."""

# authorship information
__author__ = 'Scott Crowe'
__email__ = 'sb.crowe@gmail.com'
__license__ = 'MIT'


def collatz_conjecture(number):
    """ Computes Collatz conjecture progression number, the steps required to reach 1 for some number > 1, where
    1) even numbers are divided by 2.
    2) odd numbers are multiplied by 3, then incremented by 1.

    Args:
        number (int): The initial integer, greater than 1.
    """
    assert number > 1
    count = 0
    while number != 1:
        count += 1
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
    return count

# run test cases
test_cases = [9, 97, 871, 6171, 77031, 837799, 8400511, 63728127, 670617279, 9780657631, 75128138247]
test_answers = [19, 118, 178, 261, 350, 524, 685, 949, 986, 1132, 1228]
case_answers = []
for case in test_cases:
    case_answers.append(collatz_conjecture(case))
    print(str(case) + ': ' + str(case_answers[-1]))
print()
print('Test passed: ' + str(case_answers == test_answers))