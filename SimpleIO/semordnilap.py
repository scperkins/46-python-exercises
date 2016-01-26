#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
According to Wikipedia, a semordnilap is a word or phrase that spells a
different word or phrase backwards. ("Semordnilap" is itself "palindromes"
spelled backwards.) Write a semordnilap recogniser that accepts a file name
(pointing to a list of words) from the user and finds and prints all pairs of
words that are semordnilaps to the screen. For example, if "stressed" and
"desserts" is part of the word list, the the output should include the pair
"stressed desserts". Note, by the way, that each pair by itself forms a
palindrome!
"""

def is_semordnilap(word, next_word):
    if word == next_word[::-1]:
        return True

def read_file():
    results = {}
    f = open('resources/semordnilap.txt', 'r')
    words = f.read().split()
    for word in words:
        for next_word in words:
            if is_semordnilap(word, next_word):
                results[word] = next_word
    return results

if __name__ == "__main__":
    print(read_file())
