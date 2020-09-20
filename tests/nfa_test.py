import pytest
from simulator import *
from example_nfa import *

def test_even_0_or_1():
    trace = [(None, 4), ('1', 5), ('0', 5), ('0', 5), ('0', 5), ('1', 4)]
    assert even_0_or_1.oracle(trace, True)