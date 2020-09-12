#!/usr/bin/env python

import pytest
from simulator import *

def test_alphabet_init():
    a = Alphabet('A', 'B', 1,2,3)
    assert a.alphabet == ['A', 'B', 1, 2, 3]


def test_alphabet_rand_string():
    a = Alphabet('A', 'B', 1,2,3)
    rand_string = a.gen_rand_string(5)
    assert len(rand_string) == 5
    assert all(x in a.alphabet for x in rand_string)


def test_nth_string():
    a = Alphabet(1,2,3,4,5)
    assert a.lexi(0) == []
    assert a.lexi(1) == [1]
    assert a.lexi(25) == [4,5]
    a = Alphabet(1,2,3)
    assert a.lexi(25) == [2,2,1]

def test_dfa_no_string():
    DFA([1],
        lambda a: 1,
        1,
        [])

def test_dfa_empty_string():
    DFA([1,2],
        lambda a: 2,
        1,
        [1])
