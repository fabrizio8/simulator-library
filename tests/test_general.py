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
    dfa = DFA({1},
        lambda s,c: 1,
        1,
        {})
    assert not dfa.accepted('')
    assert not dfa.accepted('a')
    assert not dfa.accepted('abasdg')

# task 6
def test_dfa_empty_string():
    dfa = DFA({1,2},
        lambda s,c: 2,
        1,
        {1})
    assert dfa.accepted('')
    assert not dfa.accepted('a')
    assert not dfa.accepted('aaaa')

# task 7
def test_dfa_accepts_only_string_of_exactly_arg():
    dfa = gen_DFA_that_accepts_strings_of_exactly_arg('a')
    assert dfa.accepted('a')
    assert not dfa.accepted('aa')
    assert not dfa.accepted('b')
    assert not dfa.accepted('')

def test_complement():
    dfa = gen_DFA_that_accepts_strings_of_exactly_arg('a')
    dfa_c = dfa.complement()
    assert dfa_c.accepted('aa')
    assert dfa_c.accepted('')
    assert dfa_c.accepted('asdasf')
    assert dfa_c.accepted('asdadgdgsd')
    assert not dfa_c.accepted('a')

def test_dfa_to_nfa():
    dfa = gen_DFA_base_b_divisible_by_n(10,5)
    nfa = dfa.to_NFA()
    assert nfa.accepted('25')
