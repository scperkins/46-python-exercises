#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Represent a small bilingual lexicon as a Python dictionary in the following
fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"år"} and use it to translate your Christmas cards from
English into Swedish. That is, write a function translate() that takes a list
of English words and returns a list of Swedish words.
"""

TRANSLATIONS = {
    'merry': 'god',
    'christmas': 'jul',
    'and': 'och',
    'happy': 'gott',
    'new': 'nytt',
    'year': 'ar',
}

def translate(english_words):
    swedish = []
    for word in english_words:
        for k, v in TRANSLATIONS.items():
            if k == word:
                swedish.append(v)
    return swedish 

if __name__ == "__main__":
    print(translate(['merry', 'christmas', 'and', 'happy', 'new', 'year']))
