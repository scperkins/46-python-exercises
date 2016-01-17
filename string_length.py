#-*- coding: utf-8 -*-
#! /usr/bin/env python

"""
Define a function that computes the length of a given list or string. (It is
true that Python has the len() function built in, but writing it yourself is
nevertheless a good exercise.)
"""
import string
import random

def string_length(my_string):
    return sum(1 for l in my_string)

if __name__ == "__main__":
    rand = random.randint(0,100)
    random_string =''.join(random.choice(string.ascii_lowercase) for _ in range(rand))
    print('Standard len method:', len(random_string))
    print('My len method:', string_length(random_string))
