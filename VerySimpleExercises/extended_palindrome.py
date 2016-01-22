#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a version of a palindrome recognizer that also accepts phrase palindromes
such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on
no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan,
oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that
punctuation, capitalization, and spacing are usually ignored.
"""

import string

def is_extended_palindrome(sentence):
    sentence = ''.join([word for word in sentence.lower().split()])
    sentence = ''.join([char for char in sentence if char not in string.punctuation])
    if sentence == sentence[::-1]:
        return True

if __name__ == "__main__":
    print(is_extended_palindrome("Sit on a potato pan, Otis"))
