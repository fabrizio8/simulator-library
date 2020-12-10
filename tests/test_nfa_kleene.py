from simulator import *
from example_nfa import *

def test_a():
    a = kleene_star(even_0_or_1)
    assert a._accepted('')
    assert a._accepted('1')
    assert a._accepted('10')

def test_b():
    a = kleene_star(third_from_last_is_0)
    assert a._accepted('111100011000')

def test_c():
    a = kleene_star(is_one)
    assert a._accepted('1')
    assert not a._accepted('0')
    assert a._accepted('1111')

def test_d():
    a = concat_nfa(is_zero_or_one, is_zero_or_one)
    assert a._accepted('11')
    assert not a._accepted('111')
    a = kleene_star(a)
    assert a._accepted('11')
    assert a._accepted('101010')
    assert a._accepted('1010101111')

def test_compile():

    a = compile(kleene_star(even_0_or_1))
    assert a.accepted('')
    assert a.accepted('1')
    assert a.accepted('10')
