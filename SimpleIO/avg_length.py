#! /usr/bin/env python
# -*_ coding: utf-8 -*-
"""
Write a program that will calculate the average word length of a text stored in
a file (i.e the sum of all the lengths of the word tokens in the text, divided
by the number of word tokens).
"""
import re

def avg_length(filename):
    f = open(filename, 'r')
    words = re.findall('\w+', f.read())
    return sum([len(word) for word in words]) / len(words)

if __name__ == "__main__":
    print(avg_length('resources/avg.txt'))

