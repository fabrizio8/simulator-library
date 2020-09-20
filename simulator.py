from random import randint
from typing import Any, Callable, Dict, List, Tuple
from collections import deque
from itertools import combinations, product
from util import *
from string import digits

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


class NFA:
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

    def epsilon_transition(self, state):
        stack = [state]
        encountered = set()

        while stack:
            state = stack.pop()
            if state not in encountered:
                encountered.add(state)
                if None in self.delt[state]:
                    stack.extend(self.delt[state][None])

        return encountered

    
    def oracle(self, trace: List[Tuple[Any,Any]], assertion):
        current_state = self.q
        print(self.delt[current_state].get(None))
        for step in trace:
            c, state = step
            if state not in self.delt[current_state].get(c):
                return True if assertion is False else False
            current_state = state
        return True if assertion is True else False

        
    
    def accepted(self, string, trace=False):
        state = self.q
        output = ""
        output += "{}".format(state)
        for c in string:
            output += ","
            state = self.delt(state,c)
            output += "{}".format(state)
        if trace:
            print(output)

        return True if state in self.F else False

    def __str__(self):
        return 'Q: {}\ndelta: {}\nq: {}\nF: {}\nsigma{}'.format(self.Q,self.delt,self.q,self.F,self.sigma)

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

    def accepted(self, string, trace=False):
        state = self.q
        output = ""
        output += "{}".format(state)
        for c in string:
            output += ","
            state = self.delt(state,c)
            output += "{}".format(state)
        if trace:
            print(output)

        return True if state in self.F else False

    
    def complement(self):
        return DFA(self.Q,
                    self.delt,
                    self.q,
                    self.Q - self.F,
                    self.sigma)

    def to_NFA(self):
        return NFA(self.Q,
                   lambda s,c: self.delt(s,c) if c is not None else None,
                   self.q,
                   self.F,
                   self.sigma)


    def __str__(self):
        return 'Q: {}\ndelta: {}\nq: {}\nF: {}\nsigma{}'.format(self.Q,self.delt,self.q,self.F,self.sigma)


def union(A, B):
    return DFA(
               set(product(A.Q, B.Q)),
               lambda s,c: (try_delta(A.delt,s[0], c), try_delta(B.delt,s[1],c)),
               (A.q, B.q),
               set(product(A.F, B.Q))|(set(product(A.Q, B.F))),
               A.sigma|B.sigma,
              )

def intersect(A, B):
    return DFA(
               set(product(A.Q, B.Q)),
               lambda s,c: (try_delta(A.delt,s[0], c), try_delta(B.delt,s[1],c)),
               (A.q, B.q),
               set(product(A.F, B.F)),
               A.sigma|B.sigma,
              )

def subset(A, B):
    return (find_accepted_string(intersect(A, B.complement())) is not None) == False

def equal(A,B):
    return subset(A,B) and subset(B,A)

def gen_DFA_that_accepts_strings_of_exactly_arg(x):
    return DFA({1,2,3},
                lambda s,c: { 1: 2 if c==x else 3,
                              2: 3,
                              3: 3, }[s],
                1,
                {2})

def gen_DFA_base_b_divisible_by_n(b,n):
    accept_s = start_s = '0'
    d_table = { str(state):
            { str(symbol): None for symbol in range(b) } for state in range(n)
          }

    d_table[None] = {None:None}
    d_table[start_s]['0'] = accept_s
    lookup = { '0': accept_s }.setdefault
    for num in range(n*b):
        end_s = str(num%n)
        num_s = num_to_baseN_str(num,b)
        before_end_state = lookup(num_s[:-1],start_s)
        d_table[before_end_state][num_s[-1]] = end_s
        lookup(num_s, end_s)

    return DFA(set(d_table.keys()),
            lambda s,c: d_table[s][c],
            '0',
            {'0'},
            set(digits))

