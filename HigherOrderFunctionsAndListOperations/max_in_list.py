#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using the higher order function reduce(), write a function max_in_list() that
takes a list of numbers and returns the largest one. Then ask yourself: why
define and call a new function, when I can just as well call the reduce()
function directly?
"""

from functools import reduce
import unittest

def max_in_list(nums):
    return reduce(max, nums)

class TestMaxReduce(unittest.TestCase):
     def test_max_in_list(self):
         nums = [1,3,14,200,130]
         self.assertEqual(max_in_list(nums), 200)

if __name__ == "__main__":
    unittest.main()
