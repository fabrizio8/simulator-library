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
    assert a.get_nth_string(25) == (4,4)
    a = Alphabet(1,2,3)
    assert a.get_nth_string(25) == (2,1,3)
    print("begin")
    for i in range(10):
        print(a.get_nth_string(i))
