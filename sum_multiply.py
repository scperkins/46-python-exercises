#-*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Define a function sum() and a function multiply() that sums and multiplies
(respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3,
4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""

from functools import reduce

def _sum(nums):
    return reduce((lambda x,y: x+y), nums)

def _multiply(nums):
    return reduce((lambda x, y: x*y), nums)

if __name__ == "__main__":
    print(_sum([1,2,3,4]))
    print(_multiply([1,2,3,4]))
