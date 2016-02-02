#1 /usr/bin/env python
# -*- coding: utf-8 -*=
"""
An anagram is a type of word play, the result of rearranging the letters of a
word or phrase to produce a new word or phrase, using all the original letters
exactly once; e.g., orchestra = carthorse. Using the word list at
http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds
the sets of words that share the same characters that contain the most words in
them.
"""
from collections import defaultdict

def find_anagrams(filename):
    words =[]
    with open(filename) as f:
        for line in f:
            words.append(line.rstrip())
    
    anagram_dict = defaultdict(list)
    for word in words:
        anagram_dict[''.join(sorted(word))].append(word)
        #anagram_dict[key].append(word)

    longest_agm = 0
    for anagram, words in anagram_dict.items():
        if len(words) > longest_agm:
            longest_agm = len(words)
    
    for anagram, words in anagram_dict.items():
        if len(words) > longest_agm - 1:
            print(anagram, words)

if __name__ == "__main__":
    find_anagrams('resources/wordlist.txt')
