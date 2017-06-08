# -*- coding: utf-8 -*-
""" Solutions to Project Euler problems 1-50, available at https://projecteuler.net/archives """

# authorship information
__author__ = 'Scott Crowe'
__email__ = 'sb.crowe@gmail.com'
__license__ = 'MIT'

# import libraries
import math


def problem_01_multiples_3_5(limit):
    """ Problem 1: Calculates the sum of all multiples of 3 or 5 below limit.

    Args:
        limit (int): The limit below which numbers are checked.
    """
    multiple_sum = 0
    for number in range(limit):
        if number % 3 == 0 or number % 5 == 0:
            multiple_sum += number
    return multiple_sum


def problem_02_fibonacci_sum(limit):
    """ Problem 2: Calculates the sum of all even terms in Fibonacci sequence below limit.

    Args:
        limit (int): The limit below which even numbers are summed.
    """
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] < limit:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    sum_even_terms = 0
    for term in fibonacci_sequence:
        if term % 2 == 0:
            sum_even_terms += term
    return sum_even_terms


def problem_03_prime_factor(number):
    """ Problem 3: Determines the largest prime factor for a number.

    Args:
        number (int): The number to determine the largest prime factor of.
    """
    def prime_factors(case):
        result = []
        if case % 2 and case > 2 == 0:
            result.append(2)
            result.extend(prime_factors(case / 2))
        for divisor in range(3, int(math.sqrt(case)) + 2, 2):
            if case % divisor == 0:
                result.extend(prime_factors(divisor))
                result.extend(prime_factors(case / divisor))
        if len(result) == 0:
            result.append(case)
        return sorted(result)

    return max(prime_factors(number))


def problem_04_palindrome_product(digits):
    """ Problem 4: Determines the largest palindrome product of two numbers with set number of digits.

    Args:
        digits (int): The number of digits in the factors.
    """
    result = 0
    max_factor = int(1 * 10 ** digits) - 1
    first_range = range(max_factor, 0, -1)
    for first in first_range:
        # check if larger product is possible
        if result / first > max_factor:
            return result
        second_range = range(first, 0, -1)
        for second in second_range:
            product = first * second
            if product > result:
                if str(product) == str(product)[::-1]:
                    result = product


def project_05_smallest_divisible(set):
    """ Problem 5: Determine the smallest number divisible by all numbers in the set.

    Args:
        set (list): The numbers that must be factors of product.
    """
    product = 1
    # remove redundant set elements
    factors = list(set)
    for test_factor in set:
        for test_product in set:
            if test_product > test_factor and test_product % test_factor == 0:
                factors.remove(test_factor)
                break
    # determine upper ceiling of search
    for number in factors:
        product = int(int(product) * int(number))
    for value in range(max(set), product, max(set)):
        divisible = True
        for factor in factors:
            if value % factor is not 0:
                divisible = False
                break
        if divisible:
            return value
    return product


def project_06_sum_square_difference(count):
    """ Problem 6: Determines the difference between the sum of squares and square of sum of defined count of numbers.

    Args:
        count (int): The count of natural numbers, beginning from 1.
    """
    set = range(1, count + 1, 1)
    square_sum = sum(set) ** 2
    sum_squares = 0
    for term in set:
        sum_squares += term ** 2
    return square_sum - sum_squares


def project_07_prime_number(index):
    """ Problem 7: Determines the nth prime number.

    Args:
        index (int): The count of prime numbers.
    """
    primes = [2]
    term = 3
    while len(primes) < index:
        add_term = True
        for prime in primes:
            if term % prime == 0:
                add_term = False
                break
        if add_term:
            primes.append(term)
        term += 1
    return primes[-1]


def project_08_largest_product(count):
    """ Problem 8: Find the largest product of n numbers in a hardcoded series..

    Args:
        count (int): The number of adjacent numbers to determine product for.
    """
    def product(sequence):
        if 0 in sequence:
            return 0
        else:
            product = 1
            for term in sequence:
                product = int(int(product) * int(term))
            return product
    series = '73167176531330624919225119674426574742355349194934' \
             '96983520312774506326239578318016984801869478851843' \
             '85861560789112949495459501737958331952853208805511' \
             '12540698747158523863050715693290963295227443043557' \
             '66896648950445244523161731856403098711121722383113' \
             '62229893423380308135336276614282806444486645238749' \
             '30358907296290491560440772390713810515859307960866' \
             '70172427121883998797908792274921901699720888093776' \
             '65727333001053367881220235421809751254540594752243' \
             '52584907711670556013604839586446706324415722155397' \
             '53697817977846174064955149290862569321978468622482' \
             '83972241375657056057490261407972968652414535100474' \
             '82166370484403199890008895243450658541227588666881' \
             '16427171479924442928230863465674813919123162824586' \
             '17866458359124566529476545682848912883142607690042' \
             '24219022671055626321111109370544217506941658960408' \
             '07198403850962455444362981230987879927244284909188' \
             '84580156166097919133875499200524063689912560717606' \
             '05886116467109405077541002256983155200055935729725' \
             '71636269561882670428252483600823257530420752963450'
    max_terms = list(map(int, series[0:count]))
    max_product = product(max_terms)
    for start_index in range(1, len(series)-count-1, 1):
        terms = list(map(int, series[start_index:start_index+count]))
        term_product = product(terms)
        if term_product > max_product:
            max_terms = terms
            max_product = term_product
    return max_product


def project_09_pythagorean_triplet(summation):
    """ Problem 9: Find the product of pythagorean triplet a, b, c, that sums to user specified total.

    Args:
        summation (int): The sum of a + b + c.
    """
    for a in range(0,int(summation/3)+1,1):
        for b in range(a+1, int(summation/2)+1,1):
            c = summation - b - a
            if c > b > a:
                if c**2 == a**2 + b**2:
                    return a*b*c
    return None


def problem_10_sum_primes(limit):
    """ Problem 10: Sum all primes below limit.

    Args:
        limit (int): The limit for primes to sum.
    """
    sieve = list(range(0, limit+1, 1))
    sieve[1] = 0
    for factor in range(2, int(math.sqrt(limit)) + 1, 1):
        for multiple in range(2, int(limit / factor) + 1, 1):
            sieve[int(factor * multiple)] = 0
    return sum(sieve)


def problem_25_fibonacci_digit_length(digits):
    """ Problem 25: Find the index of the first term in the Fibonacci sequence to contain specified number of digits.

    Args:
        digits (int): The number of digits.
    """
    curr_index = 3
    curr_term = 2
    prev_term = 1
    prev_prev_term = 1
    while len(str(curr_term)) < digits:
        prev_prev_term = prev_term
        prev_term = curr_term
        curr_term = prev_prev_term + prev_term
        curr_index += 1
    return curr_index


def problem_30_narcissistic_number(power):
    """ Problem 30: Find sum of numbers that can be written as the sum of powers of their digits.

    Args:
        power (int): The exponent of the digits.
    """
    # find limit to search
    limit = len(str(9**power))*(9**power)
    valid_numbers = []
    for number in range(2, limit, 1):
        sum_of_powers_of_digits = 0
        for char in str(number):
            sum_of_powers_of_digits += int(char) ** power
        if sum_of_powers_of_digits == number:
            valid_numbers.append(number)
    return sum(valid_numbers)


def problem_48_self_powers(series_limit, digits):
    """ Problem 48: Find the last digits of series n^n (n = 1 to series limit).

    Args:
        series_limit (int): The maximum base and power in the series.
        digits (int): The number of last digits to take from sum.
    """
    result = 0
    for number in range(1, series_limit + 1, 1):
        result += number ** number
    return str(result)[-digits:]

# run problems
print("Problem 1 - Sum of all multiples of 3 or 5 below 1000: " + str(problem_01_multiples_3_5(1000)))
print("Problem 2 - Sum of even valued terms in Fibonacci sequence < 4 million: " + str(problem_02_fibonacci_sum(4000000)))
print("Problem 3 - Largest prime factor of 600851475143: " + str(problem_03_prime_factor(600851475143)))
print("Problem 4 - Largest palindrome product of two 3 digit numbers: " + str(problem_04_palindrome_product(3)))
print("Problem 5 - Smallest number divisible by 1 to 20: " + str(project_05_smallest_divisible(range(1, 21, 1))))
print("Problem 6 - Difference between sum of squares and square of sums (1-10): " + str(project_06_sum_square_difference(100)))
print("Problem 7 - Determine the 10001st prime number: " + str(project_07_prime_number(10001)))
print("Problem 8 - Determine largest product in series: " + str(project_08_largest_product(13)))
print("Problem 9 - Find pythagorean triplet where a + b + c = 1000: " + str(project_09_pythagorean_triplet(1000)))
print("Problem 10 - Sum of all primes < 2,000,000: " + str(problem_10_sum_primes(2000000)))
print("Problem 25 - Index of first Fibonacci term containing 1000 digits: " + str(problem_25_fibonacci_digit_length(1000)))
print("Problem 30 - Sum of all numbers the sum of the fifth powers of their digits: " + str(problem_30_narcissistic_number(5)))
print("Problem 48 - Last 10 digits of sum of series n^n, from 1 to 1000: " + problem_48_self_powers(1000, 10))