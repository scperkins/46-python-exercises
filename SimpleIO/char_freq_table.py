#! /usr/bin/env python
#-*- coding: utf-8 -*-
"""
Write a procedure char_freq_table() that, when run in a terminal, accepts a
file name from the user, builds a frequency listing of the characters contained
in the file, and prints a sorted and nicely formatted character frequency table
to the screen.
"""
from collections import defaultdict
from prettytable import PrettyTable
from operator import itemgetter

def char_freq_table(filename):
    d = defaultdict(int)
    f = open(filename, 'r')
    chars = f.read().split()
    for char in chars[0]:
        d[char] += 1
    return d
            
if __name__ == "__main__":
    results = char_freq_table('resources/randomchars.txt') 
    table = PrettyTable(["Character", "Frequency"])
    for k, v in results.items():
        table.add_row([k, v])
    print(table)
