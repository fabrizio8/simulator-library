from simulator import *
from example_nfa import *

def test_a():
    huge = concat_nfa(even_0_or_1,ends_in_1)
    for nfa in nfa_list[3:]:
        huge = concat_nfa(huge, nfa)

    assert huge._accepted('0000000000000')
    assert huge._accepted('1111111111111')
    assert huge._accepted('1010101010101')
    assert huge._accepted('111111111111')

    assert not huge._accepted('00000c')
    assert not huge._accepted('11111b')
    assert not huge._accepted('1a0101')
    assert not huge._accepted('11bcdcd111111')

def test_b():
    a = concat_nfa(even_0_or_1, ends_in_1)
    assert a._accepted('1111111111111')
    assert a._accepted('00')
    assert a._accepted('0000')
    assert a._accepted('111111')
    assert not a._accepted('111110')
