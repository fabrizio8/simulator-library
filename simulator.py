from random import randint
from itertools import product
from math import log, ceil

class Alphabet:
    alphabet = []
    def __init__(self, *args):
        self.alphabet = [*args]
    def gen_rand_string(self, length):
        return [self.alphabet[c] for c in [randint(0,length-1) for _ in range(length)]] 
    def get_nth_string(self, n):
        if n == 0:
            return list(product(self.alphabet, repeat=1))[0]
        exp = ceil(log(n, len(self.alphabet)))
        idx = n-sum(len(self.alphabet)**x for x in range(exp))
        return list(product(self.alphabet, repeat=exp))[idx-1]
