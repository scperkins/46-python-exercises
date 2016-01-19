#! /usr/bin/env python
# -*_ coding: utf-8 -*-
"""
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words.
"""

def word_map(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

if __name__ == "__main__":
    print(word_map(['hello', 'I', 'test', 'hsuygsusg']))
