#-*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Define a function reverse() that computes the reversal of a string. For
example, reverse("I am testing") should return the string "gnitset ma I".
"""

def _reverse(string):
    return string[::-1]

if __name__ == "__main__":
    print(_reverse('Reverse my string!'))
