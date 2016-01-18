#-*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Define a function overlapping() that takes two lists and returns True if they
have at least one member in common, False otherwise. You may use your
is_member() function, or the in operator, but for the sake of the exercise, you
should (also) write it using two nested for-loops.
"""

def overlapping(list1, list2):
    for elem in list1:
        for i in list2:
            if elem == i:
                return True
    return False

if __name__ == "__main__":
    list1 = [1,2,3,4]
    list2 = [5,6,4,7]

    list3 = [1,2,3,4]
    list4 = [5,6,7,8]

    print('Should return True:', overlapping(list1, list2))
    print('Should return False:', overlapping(list3, list4))
