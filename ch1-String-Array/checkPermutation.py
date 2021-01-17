#!/usr/bin/env python3
"""
Given two strings, write a method to decide if one a permutation of the another
"""
import unittest
from collections import Counter

def check_permutation_by_sort(str1, str2):
    if len(str1) != len(str2):
        return False
    s1, s2 = sorted(str1), sorted(str2)
    for i in range(len(s1) - 1):
        if s1[i] != s2[i]:
            return False
    return True


def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for char in str1:
        counter[ord(char)] += 1
    for char in str2:
        if counter[ord(char)] == 0:
            return False
    return True


def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


class TestCheckPermutation(unittest.TestCase):
    test_cases = [
        ('bat', 'tab', True),
        ('c982r', 'rc892', True),
        ('God', 'dog', False),
        ('good', 'notsogood', False),
        ('# 123 pqrs', 'pqrs # 123', True),
        ('loveCoding', 'LoveCoding', False),
        ('hihi', 'ihhi', True),
    ]

    test_functions = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]
    
    def test_check_permutation(self):
        for test_function in self.test_functions:
            for str1, str2, expected in self.test_cases:
                self.assertEqual(test_function(str1, str2), expected)


if __name__ == "__main__":
    unittest.main()
