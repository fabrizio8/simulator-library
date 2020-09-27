from simulator import *
from example_nfa import *

def test_general():
    a = concat_nfa(even_0_or_1, ends_in_1)
    print('a', a)
