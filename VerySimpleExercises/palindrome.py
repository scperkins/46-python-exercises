#-*_ coding: utf-8 -*-
#! /usr/bin/env python
"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that
look the same written backwards). For example, is_palindrome("radar") should
return True.
"""

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else: return False

if __name__ == "__main__":
    print('Should be a palindrome:', is_palindrome('radar'))
    print('Should NOT be a plaindrome:', is_palindrome('hello'))
