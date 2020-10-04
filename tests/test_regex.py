from example_regex import *

def test_general():
    re = RE_circ(RE_star(RE_union(RE_char('1'), RE_char('0'))),
                         RE_star(RE_union(RE_char('0'), RE_epsilon())))
    print(re)
