#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Represent a small bilingual lexicon as a Python dictionary in the following
fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"år"} and use it to translate your Christmas cards from
English into Swedish. Use the higher order function map() to write a function
translate() that takes a list of English words and returns a list of Swedish
words.
"""
import unittest

words = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
        "new":"nytt", "year":"år"}

def translate(english):
    return list(map(lambda word: words[word], english))


class TestTranslate(unittest.TestCase):

    def test_translate(self):
        self.assertEqual(translate(['merry', 'christmas', 'happy']), ['god',
            'jul', 'gott'])

if __name__ == "__main__":
    unittest.main()
