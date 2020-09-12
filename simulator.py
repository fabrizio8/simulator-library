from random import randint
from typing import Callable, Dict

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
    Q = []
    delt: Callable = None
    q = None
    F = []
    
    def __init__(self,Q,delt,q,F):
        self.Q = Q
        self.delt = delt
        self.q = q
        self.F = F


def gen_DFA_that_accepts_strings_of_exactly_arg(x):
    return DFA([1,2,3],
                lambda s,c: { 1: 2 if c==x else 3,
                              2: 3,
                              3: 3, }[s],
                1,
                [2])

def trace(dfa, string):
    state = dfa.q
    print(state, end='')
    for i in string:
        print(',',end="")
        state = dfa.delt(state,i)
        print(state, end='')
    print()
    if state in dfa.F:
        return True
    else:
        return False

