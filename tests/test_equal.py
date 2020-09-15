from simulator import *
from example_dfa import *
from itertools import combinations

def test():
    for a,b in combinations(dfas,2):
        try:
            assert not equal(a, b)
        except:
            if a is even_chars and b is strictly_alternating:
                assert equal(a,b)
