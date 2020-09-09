from random import randint
from typing import Callable

class Alphabet:
    alphabet = []
    def __init__(self, *args):
        self.alphabet = [*args]


    def gen_rand_string(self, length):
        return [self.alphabet[c] for c in [randint(0,length-1) for _ in range(length)]] 


    def lexi(self, n):
        if n == 0:
            return []
        return self.lexi((n-1)//len(self.alphabet)) + [self.alphabet[(n-1)%len(self.alphabet)]]


class DFA:
    Q: Callable = None
    sig: Alphabet = None
    delt: Callable = None
    q = None
    F: Callable = None
    
    def __init__(Q,sig,delt,q,F):
        self.Q = Q
        self.sig = sig
        self.delt = delt
        self.q = q
        self.F = F
