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


# task 5
def test_dfa_no_string():
    dfa = DFA([1],
        lambda s,c: 1,
        1,
        [])
    assert not accepted(dfa, '')
    assert not accepted(dfa, 'a')
    assert not accepted(dfa, 'abasdg')

# task 6
def test_dfa_empty_string():
    dfa = DFA([1,2],
        lambda s,c: 2,
        1,
        [1])
    assert accepted(dfa, '')
    assert not accepted(dfa, 'a')
    assert not accepted(dfa, 'aaaa')

# task 7
def test_dfa_accepts_only_string_of_exactly_arg():
    dfa = gen_DFA_that_accepts_strings_of_exactly_arg('a')
    assert accepted(dfa, 'a')
    assert not accepted(dfa, 'aa')
    assert not accepted(dfa, 'b')
    assert not accepted(dfa, '')

def test_complement():
    dfa = gen_DFA_that_accepts_strings_of_exactly_arg('a')
    #dfa_c = dfa.complement()
    #assert accepted(dfa_c, 'aa')
    #assert accepted(dfa_c, '')
    #assert accepted(dfa_c, 'asdasf')
    #assert accepted(dfa_c, 'asdadgdgsd')
    #assert not accepted(dfa_c, 'a')
