#! /usr/bin/env python
# -*- coing: utf-8 -*-
"""
Write a program able to play the "Guess the number"-game, where the number to
be guessed is randomly chosen between 1 and 20. (Source:
http://inventwithpython.com) This is how it should work when run in a terminal:

    >>> import guess_number
    Hello! What is your name?
    Torbjörn
    Well, Torbjörn, I am thinking of a number between 1 and 20.
    Take a guess.
    10
    Your guess is too low.
    Take a guess.
    15
    Your guess is too low.
    Take a guess.
    18
    Good job, Torbjörn! You guessed my number in 3 guesses!
"""
import random

if __name__ == "__main__":
    number = random.randint(1,20)

    player = input('Hello! What is your name? ')
    print('Well {}, I am thinking of a number between 1 and 20.'.format(player))
    
    guesses = 0    
    correct = False
    while not correct:
        guess = int(input('Take a guess.\n'))
        if guess > number:
            print('Your guess is too high.')
            guesses += 1
        if guess < number:
            print('Your guess is too low.')
            guesses += 1
        if guess == number:
            guesses += 1
            print('Good job, {}! You guessed my number in {} guesses!'.format(player, guesses))
            correct = True
