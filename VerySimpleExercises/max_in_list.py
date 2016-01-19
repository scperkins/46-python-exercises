# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
The function max() from exercise 1) and the function max_of_three() from
exercise 2) will only work for two and three numbers, respectively. But suppose
we have a much larger number of numbers, or suppose we cannot tell in advance
how many they are? Write a function max_in_list() that takes a list of numbers
and returns the largest one.
"""

def max_in_list(seq):
    return sorted(seq)[-1]

if __name__ == "__main__":
    print(max_in_list([1,2,3,4,10,100,87,90]))
