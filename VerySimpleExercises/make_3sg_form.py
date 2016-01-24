#! /usr/bin/env python
# _*- coding:utf-8 -*-
"""
The third person singular verb form in English is distinguished by the suffix
-s, which is added to the stem of the infinitive form: run -> runs. A simple
set of rules can be given as follows:

    If the verb ends in y, remove it and add ies
    If the verb ends in o, ch, s, sh, x or z, add es
    By default just add s

Your task in this exercise is to define a function make_3sg_form() which
given a verb in infinitive form returns its third person singular form.
Test your function with words like try, brush, run and fix. Note however
that the rules must be regarded as heuristic, in the sense that you must
not expect them to work for all cases. Tip: Check out the string method
endswith().
"""
import unittest

def make_3sg_form(verb):
    es = ('o','ch', 's', 'sh', 'x','z')
    if verb.endswith('y'):
        verb = verb[:-1]
        return verb + 'ies'
    elif verb.endswith(es):
        return verb + 'es'
    else: return verb + 's'

class Test3SGForm(unittest.TestCase):

    def test_make_3sg_form(self):
        self.assertEqual(make_3sg_form('try'), 'tries')
        self.assertEqual(make_3sg_form('brush'), 'brushes')
        self.assertEqual(make_3sg_form('run'), 'runs')
        self.assertEqual(make_3sg_form('fix'), 'fixes')

if __name__ == "__main__":
    unittest.main()
