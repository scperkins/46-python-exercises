# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a function find_longest_word() that takes a list of words and returns the
length of the longest one.
"""

def find_longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

if __name__ == "__main__":
    print(find_longest_word(['hello', 'test', 'longest', 'something']))
