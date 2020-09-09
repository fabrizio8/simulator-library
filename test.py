#!/usr/bin/env python

from itertools import product
import sys

if len(sys.argv) > 1:
    r = int(sys.argv[1])
else:
    r = 2
a = [1,2,3]
def p(i):
    count = 0
    for x in i:
        print(count, x) 
        count += 1
p(product(a, repeat=r))
