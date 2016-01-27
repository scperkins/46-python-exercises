#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once
in either the written record of a language, the works of an author, or in a
single text. Define a function that given the file name of a text will return
all its hapaxes. Make sure your program ignores capitalization.
"""
from collections import defaultdict

def is_hapax(filename):
    d = defaultdict(int)
    f = open(filename, 'r')
    words = f.read().split()
    words = [word.lower() for word in words]
    for word in words:
        d[word] += 1
    unique = []
    for k, v in d.items():
        if v == 1:
            unique.append(k)
    return unique

if __name__ == "__main__":
   print(is_hapax('resources/hapax.txt')) 
