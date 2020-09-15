from simulator import *
from example_dfa import *
from itertools import combinations

f = gen_DFA_base_b_divisible_by_n
def test_basic():
    for a,b in combinations(dfas,2):
        try:
            assert not equal(a, b)
        except:
            if a is even_chars and b is strictly_alternating:
                assert equal(a,b)

def test_union():
    assert equal(f(10,2), f(10,2))
    assert equal(union(f(10,4),f(10,2)),union(f(10,2),f(10,4)))

def test_intersect():
    for a,b in enumerate(range(1,7),2):
        equal(intersect(f(10, a), f(10,b)), f(10,a*b))

def test_complement():
    assert equal(f(10,2).complement().complement(), f(10,2))

    for dfa in dfas:
        assert equal(dfa.complement().complement(), dfa)
