#-*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Write a function that takes a character (i.e. a string of length 1) and returns
True if it is a vowel, False otherwise.
"""

VOWELS = 'aeiou'

def check_vowel(char):
    if len(char) == 1:
        if char.lower() in VOWELS:
            return True
        else:
            return False
    else:
        print('Too many characters, only need one.')

if __name__ == "__main__":
    test_1 = print(check_vowel('a'))
    test_2 = print(check_vowel('b'))
    test_3 = print(check_vowel('c'))
    test_4 = print(check_vowel('jhsjhgsg'))
