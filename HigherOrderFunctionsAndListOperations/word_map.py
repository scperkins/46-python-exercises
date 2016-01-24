#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words. Write it in three different ways: 1)
using a for-loop, 2) using the higher order function map(), and 3) using list
comprehensions.
"""
import unittest

words = ['map', 'reduce', 'functional', 'programming', 'languages', 'lambda']
# [3,6,10,11,9,6]

def map_1(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

def map_2(words):
    return list(map(len, words))

def map_3(words):
    return [len(word) for word in words]

class TestWordMaps(unittest.TestCase):

    def test_map1(self):
        self.assertEqual(map_1(words), [3,6,10,11,9,6])

    def test_map_2(self):
        self.assertEqual(map_2(words), [3,6,10,11,9,6])

    def test_map_3(self):
        self.assertEqual(map_3(words), [3,6,10,11,9,6])
       
if __name__ == "__main__":
    unittest.main()
