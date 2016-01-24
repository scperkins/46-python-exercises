#! /usr/bin/env python
#-*- coding: utf-8 -*-
"""
Define a simple "spelling correction" function correct() that takes a string
and sees to it that 1) two or more occurrences of the space character is
compressed into one, and 2) inserts an extra space after a period if the period
is directly followed by a letter. E.g. correct("This   is  very funny  and
cool.Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use
regular expressions!
"""
import re
import unittest

def correct(string):
    return re.sub(r'\.(?! )', '. ', re.sub(r' +', ' ', string))

class TestSpellCheck(unittest.TestCase):

    def test_correct(self):
        self.assertEquals(correct('This is very funny and cool. Indeed!'),
                'This is very funny and cool. Indeed!')

if __name__ == "__main__":
    unittest.main()
