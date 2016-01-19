#! /usr/bin/env python
#-*- coding: utf-8 -*-
"""
Write a function filter_long_words() that takes a list of words and an integer
n and returns the list of words that are longer than n.
"""

def filter_longest_words(words, n):
    longer = []
    for word in words:
        if len(word) > n:
            longer.append(word)
    return longer

if __name__ == "__main__":
    print(filter_longest_words(['short', 'longer', 'longest', 'capitalize',
        'merger'], 5))
