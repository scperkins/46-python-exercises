#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
In a game of Lingo, there is a hidden word, five characters long. The object of
the game is to find this word by guessing, and in return receive two kinds of
clues: 1) the characters that are fully correct, with respect to identity as
well as to position, and 2) the characters that are indeed present in the word,
but which are placed in the wrong position. Write a program with which one can
play Lingo. Use square brackets to mark characters correct in the sense of 1),
and ordinary parentheses to mark characters correct in the sense of 2).
Assuming, for example, that the program conceals the word "tiger", you should
be able to interact with it in the following way:

    >>> import lingo
    snake
    Clue: snak(e)
    fiest
    Clue: f[i](e)s(t)
    times
    Clue: [t][i]m[e]s
    tiger
    Clue: [t][i][g][e][r]
"""
import random

words = ['snake', 'tiger', 'bear', 'lion', 'eagle', 'horse', 'giraffe']
word = random.choice(words)
guess = input('Welcome to Lingo! Guess the word:\n')

while guess != word:
    if guess == word:
        print('Correct!')
    clue = ''
    for letter in guess:
        if letter in word:
            if word.index(letter) == guess.index(letter):
                clue += '[{}]'.format(letter)
            else:
                clue += '({})'.format(letter)
        else: clue += letter
    print('Clue:', clue)
    guess = input('Welcome to Lingo! Guess the word:\n') 
