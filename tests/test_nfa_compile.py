from simulator import *
from example_nfa import *

def test_general():
    a = compile(even_0_or_1)
    b = compile(ends_in_1)
    print(b)
    assert not b.accepted("0010")
    assert not b.accepted("")
    assert not b.accepted("10")
    assert b.accepted("111")
    assert b.accepted("101")
    assert b.accepted("100001")
