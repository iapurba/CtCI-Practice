#!/usr/bin/env python3
"""
Implement and algorithm to determine if a string has all unique characters.
What if you cannot use aditional data structure?
"""
import unittest


def is_unique_chars_algorithmic(string):
    # assuming the character set is ASCII
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        else:
            char_set[val] = True
    return True


def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string)


class TestIsUnique(unittest.TestCase):
    test_cases = [
        ('', True),
        ('abcdef', True),
        ('cracking the coding interview', False),
        ('dwg324sp', True),
        ('!2#dCT*8 )_', True),
        (''.join([chr(val) for val in range(128)]), True)
    ]
    test_functions = [
        is_unique_chars_algorithmic,
        is_unique_chars_pythonic,
    ]

    def test_is_unique_chars(self):
        for test_function in self.test_functions:
            for testcase, expected in self.test_cases:
                self.assertEqual(test_function(testcase), expected)


if __name__ == "__main__":
    unittest.main()
