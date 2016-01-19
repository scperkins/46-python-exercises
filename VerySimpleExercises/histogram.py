#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Define a procedure histogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7]) should print the
following:

    ****
    *********
    *******
"""

def histogram(seq):
    for num in seq:
        print(num * '*')

if __name__ == "__main__":
    test = histogram([4,9,7])
