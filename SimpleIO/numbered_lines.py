#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a program that given a text file will create a new text file in which all
the lines from the original file are numbered from 1 to n (where n is the
number of lines in the file).
"""

def number_lines(filename):
    with open(filename, 'r') as f:
        out = open('resources/numbered.txt', 'w')
        for line, text in enumerate(f):
            out.write("{} {}".format(line + 1, text))
        out.close()
    out.close()

if __name__ == "__main__":
    number_lines('resources/unnumbered.txt')
