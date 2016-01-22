#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a function char_freq() that takes a string and builds a frequency listing
of the characters contained in it. Represent the frequency listing as a Python
dictionary. Try it with something like
char_freq("abbabcbdbabdbdbabababcbcbab").
"""
from collections import defaultdict

def char_freq(string):
    d = defaultdict(int)
    for char in string:
        d[char] += 1
    return d

if __name__ == "__main__":
    print(char_freq("abbabcbdbabdbdbabababcbcbab"))
