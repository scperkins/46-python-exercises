# -*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Write a function translate() that will translate a text into "rövarspråket"
(Swedish for "robber's language"). That is, double every consonant and place an
occurrence of "o" in between. For example, translate("this is fun") should
return the string "tothohisos isos fofunon".
"""

CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def translate(x):
    return ''.join(l + 'o' + l if l in CONSONANTS  else l for l in x)

if __name__ == "__main__":
    test = print(translate('dont be such a dickhead'))

