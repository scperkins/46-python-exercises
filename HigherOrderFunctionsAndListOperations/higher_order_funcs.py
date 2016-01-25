#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implement the higher order functions map(), filter() and reduce(). (They are
built-in but writing them yourself may be a good exercise.)
"""

def _map(func, iterable):
    res = []
    for x in interable:
        res.append(func(x))
    return res

def _filter(func, sequence):
    """
    An item will be produced by the iterator result of filter(function,
    sequence) if item is included in the sequence "sequence" and if
    function(item) returns True. 
    """
    return [elem for elem in sequence if func(i)]

def _reduce(func, sequence):
    for elem in sequence:
        aggregate = func(aggregate, x)
    return aggregate

if __name__ == "__main__":
    pass
