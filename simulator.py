from random import randint
from typing import Callable, Dict
from collections import deque
from itertools import combinations, product
from util import *

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

'''
Q is a finite set called the states,
Σ is a finite set called the alphabet,
δ : Q × Σ→Q is the transition function
q 0 ∈ Q is the start state, and
F ⊆ Q is the set of accept states
'''
class DFA:
    Q = set()
    delt: Callable = None
    q = None
    F = set()
    sigma = set()
    
    def __init__(self,Q,delt,q,F,sigma=None):
        self.Q = Q
        self.delt = delt
        self.q = q
        self.F = F
        self.sigma = sigma

    
    def complement(self):
        return DFA(self.Q,
                    self.delt,
                    self.q,
                    self.Q - self.F,
                    self.sigma)

    def __str__(self):
        print('Q: ', self.Q)
        print('delta: ', self.delt)
        print('q', self.q)
        print('F', self.F)
        print('sigma', self.sigma)



def union(A, B):
    return DFA(
               set(product(A.Q, B.Q)),
               lambda s,c: (A.delt(s[0], c), B.delt(s[1],c)),
               (A.q, B.q),
               set(product(A.F, B.Q))|(set(product(A.Q, B.F))),
               A.sigma|B.sigma,
              )

def intersect(A, B):
    return DFA(
               set(product(A.Q, B.Q)),
               lambda s,c: (A.delt(s[0], c), B.delt(s[1],c)),
               (A.q, B.q),
               set(product(A.F, B.F)),
               A.sigma|B.sigma,
              )

def subset(A, B):
    return bool(find_accepted_string(intersect(A, B.complement()))) == False

def equal(A,B):
    return subset(A,B) and subset(B,A)

def gen_DFA_that_accepts_strings_of_exactly_arg(x):
    return DFA({1,2,3},
                lambda s,c: { 1: 2 if c==x else 3,
                              2: 3,
                              3: 3, }[s],
                1,
                {2})

def accepted(dfa, string, trace=False):
    state = dfa.q
    if trace:
        print(state, end='')
    for c in string:
        if trace:
            print(',',end="")
        state = dfa.delt(state,c)
        if trace:
            print(state, end='')
    if trace:
        print()
    if state in dfa.F:
        return True
    else:
        return False
