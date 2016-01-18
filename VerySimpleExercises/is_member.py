#-*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Write a function is_member() that takes a value (i.e. a number, string, etc) x
and a list of values a, and returns True if x is a member of a, False
otherwise. (Note that this is exactly what the in operator does, but for the
sake of the exercise you should pretend Python did not have this operator.)
"""

def is_member(elem, seq):
    #We're going to try this without using the 'in' operator at all.
    i = 0
    while i < len(seq):
        if elem == seq[i]:
            return True
        i += 1

if __name__ == "__main__":
    print('Should return True:', is_member('a', ['b','c','d','a']))
    print('Should return None:', is_member('a', ['z','x','f','c']))
