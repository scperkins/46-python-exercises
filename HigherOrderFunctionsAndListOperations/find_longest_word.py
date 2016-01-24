#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a function find_longest_word() that takes a list of words and returns the
length of the longest one. Use only higher order functions
"""
import unittest

words = ['this','is','a','boring','list']
# [4,2,1,6,4]

def find_longest_word(words):
    return max(map(len, words))

class TestFindLongest(unittest.TestCase):

    def test_find_longest_word(self):
        self.assertEqual(find_longest_word(words), 6)

if __name__ == "__main__":
    unittest.main()
