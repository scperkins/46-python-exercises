#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a version of a palindrome recogniser that accepts a file name from the
user, reads each line, and prints the line to the screen if it is a palindrome.
"""

def read_file(filepath):
    f = open(filepath, 'r')
    for line in f.read().split('\n'):
        if is_palindrome(line):
            print(line)

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else: return False

if __name__ == "__main__":
    read_file('resources/palindrome.txt')
