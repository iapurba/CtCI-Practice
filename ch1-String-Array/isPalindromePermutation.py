import unittest
from collections import Counter


def is_permutation_of_a_palindrome_pythonic(phrase):
    counter = Counter(phrase.replace(" ", "").lower())
    return sum([val%2 for val in counter.values()]) <= 1
