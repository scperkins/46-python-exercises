#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
In English, the present participle is formed by adding the suffix -ing to the
infinite form: go -> going. A simple set of heuristic rules can be given as
follows:

    If the verb ends in e, drop the e and add ing (if not exception: be, see,
    flee, knee, etc.)
    If the verb ends in ie, change ie to y and add ing
    For words consisting of consonant-vowel-consonant, double the final letter
    before adding ing
    By default just add ing
Your task in this exercise is to define a function make_ing_form() which
given a verb in infinitive form returns its present participle form. Test
your function with words such as lie, see, move and hug. However, you must
not expect such simple rules to work for all cases.
"""
import unittest

def is_vowel(char):
    vowels = 'aieou'
    if char in vowels:
        return True
    else: return False

def make_ing_form(infinitive):
    exceptions = ('be', 'see', 'flee', 'knee')
    
    if infinitive.endswith('ie'):
        infinitive = infinitive[:-2]
        return infinitive + 'ying'
    elif infinitive.endswith('e') and infinitive not in exceptions:
        infinitive = infinitive[:-1]
        return infinitive + 'ing'
    elif not is_vowel(infinitive[-1]) and is_vowel(infinitive[-2]) and not is_vowel(infinitive[-3]):
        return infinitive + infinitive[-1] + 'ing'
    else:
        return infinitive + 'ing'

class TestMakeIngForm(unittest.TestCase):
    
    def test_is_vowel(self):
        self.assertTrue(is_vowel('a'))
        self.assertFalse(is_vowel('z'))

    def test_make_ing_form(self):
        self.assertEqual(make_ing_form('lie'), 'lying')
        self.assertEqual(make_ing_form('see'), 'seeing')
        self.assertEqual(make_ing_form('move'), 'moving')
        self.assertEqual(make_ing_form('hug'), 'hugging')

if __name__ == "__main__":
    unittest.main()
