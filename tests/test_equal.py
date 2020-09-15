from simulator import *
from example_dfa import *
from itertools import combinations

def test_basic():
    for a,b in combinations(dfas,2):
        try:
            assert not equal(a, b)
        except:
            if a is even_chars and b is strictly_alternating:
                assert equal(a,b)

def test_math():
    f = gen_DFA_base_b_divisible_by_n
    assert equal(f(10,2), f(10,2))
    assert equal(union(f(10,4),f(10,2)),union(f(10,2),f(10,4)))
    for a,b in enumerate(range(1,10),2):
        equal(intersect(f(10, a), f(10,b)), f(10,a*b))
