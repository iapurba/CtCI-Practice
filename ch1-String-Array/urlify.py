#!/usr/bin/env python3

"""
Write a method to replace all spaces in a string with `%20`. You may assume the
string has sufficient space at the end to hold the additional characters and
you are given the 'true' length of the string.
"""
import unittest


def urlify_algorithmic(string, truelength):
    char_list = list(string)
    string = ""
    new_index = len(char_list)
    for i in reversed(range(truelength)):
        if char_list[i] == " ":
            char_list[new_index - 3: new_index] = "%20"
            new_index -= 3
        else:
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    return string.join(char_list)


def urlify_pythonic(string, truelength):
    return string.rstrip().replace(" ", "%20")


class TestURLify(unittest.TestCase):
    test_cases = [
        ("the boring company    ", "the%20boring%20company"),
        ("mkbhd", "mkbhd"),
        (
            "cracking the coding interview      ",
            "cracking%20the%20coding%20interview"
        ),
    ]

    test_functions = [
        urlify_algorithmic,
        urlify_pythonic,
    ]
    def test_urlify(self):
        for test_function in self.test_functions:
            for testcase, expected in self.test_cases:
                truelength = len(testcase.rstrip())
                self.assertEqual(test_function(testcase, truelength), expected)


if __name__ == '__main__':
    unittest.main()
