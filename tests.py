#!/usr/bin/env python

from simulator import *

a = Alphabet('A', 'B', 1,2,3)
assert a.alphabet == ['A', 'B', 1, 2, 3]
rand_string = a.gen_rand_string(5)
assert len(rand_string) == 5
print(rand_string)
assert all(x in a.alphabet for x in rand_string)
