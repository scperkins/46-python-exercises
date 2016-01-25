#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using the higher order function filter(), define a function filter_long_words()
that takes a list of words and an integer n and returns the list of words that
are longer than n.
"""
import unittest

words = ['another', 'dumb', 'fucking', 'list', 'charlatan']
# [7, 4, 7, 4, 9]

def filter_long_words(words, n):
    return list(filter(lambda x: len(x) > n, words))

class TestFilterLongWords(unittest.TestCase):
    
    def test_filter_long_words(self):
        self.assertEqual(filter_long_words(words, 4), ['another', 'fucking',
            'charlatan'])

if __name__ == "__main__":
    unittest.main()
