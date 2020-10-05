from simulator import *
from example_nfa import *

def test_even_0_or_1():
    tts = [
        ("(1 [(e/2 [(0/3 [(0/2 [(0/3 [(1/3 [No])])])])])(e/4 [(0/4 [(0/4 [(0/4 [(1/5 [No])])])])])])", "0001")
    ]
    for tt in tts:
        assert tt[0] == even_0_or_1.fork(tt[1])

def test_ends_in_1():
    try:
        assert "(1 [(0/1 [(0/1 [(0/1 [(1/1 [No])(1/2 [Yes])])])])])" == ends_in_1.fork('0001')
    except:
        print(ends_in_1.fork('0001'))
        assert False