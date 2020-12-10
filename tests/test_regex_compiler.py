from example_regex import *

def test_general():
    a = RE_char('1').compile()
    assert a._accepted('1')
    assert not a._accepted('0')
    assert all_zero.compile()._accepted('0')
    assert all_zero.compile()._accepted('00')
    assert all_zero.compile()._accepted('00000')
    assert all_zero.compile()._accepted('0')
