from random import randint
from typing import Any, Callable, Dict, List, Tuple, TypeVar, Union
from collections import deque
from itertools import combinations, product
from util import *
from string import digits
from anytree.exporter import DotExporter
from anytree import Node, RenderTree
from pprint import pprint

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


    def oracle(self, trace: List[Tuple[Any,Any]], assertion):
        current_state = self.q
        for step in trace:
            c, state = step
            try:
                if state not in self.delt[current_state].get(c):
                    return True if assertion is False else False
            except:
                return True if assertion is False else False
            current_state = state
        return True if assertion is True else False


    def epsilon_transition(self, state):
        stack = [state]
        transitions = set()

        while stack:
            state = stack.pop()
            if state not in transitions:
                transitions.add(state)
                if None in self.delt[state]:
                    stack.extend(self.delt[state][None])

        return transitions

    def next_states(self, current_states, c):
        next_states = set()

        for s in current_states:
            if (end_states := self.delt[s].get(c)):
                for end_state in end_states:
                    next_states.update(self.epsilon_transition(end_state))

        return next_states

    
    def fork(self, string, state='start', c=None, out="", p=False):
        if state == 'start':
            p = True
            state = self.q
        else:
            out += "({}/{} [".format('e' if c is None else c,str(state))
        states = self.epsilon_transition(state)
        for s in [s for s in states if s != state]:
            out += self.fork(string,s) + "])"
        if not string:
            if state in self.F:
                return out + "Yes"
            else:
                return out + "No"
        
        for s in self.next_states({state}, string[0]):
            out += self.fork(string[1:],s,string[0]) + "])"

        if p:
            out = "({} [".format(str(state)) + out + "])" 

        return out


    def _accepted(self, string):
        states = self.epsilon_transition(self.q)

        for c in string:
            states = self.next_states(states, c)

        return True if any(s in self.F for s in states) else False

    # naive accept function
    def accepted(self, string, trace=False, ret_trace=False):
        state = self.q
        output = ""
        trace_out = [state]
        output += "{}".format(state)
        for c in string:
            output += ","
            state = self.delt(state,c)
            output += "{}".format(state)
            trace_out.append(state)
        if trace:
            print(output)
        if ret_trace:
            return trace_out
        else:
            return True if state in self.F else False

    def __str__(self):
        return 'Q: {}\ndelta: {}\nq: {}\nF: {}\nsigma{}'.format(self.Q,self.delt,self.q,self.F,self.sigma)

def union_nfa(A, B):
    pprint(A.delt)
    print()
    pprint(B.delt)
    print()
    key_idx = max(A.delt.keys())+1
    delt = {1: {None: {2,key_idx+1}}}
    offset = 1
    for k,v in A.delt.items():
        delt[k+offset] = {k:{x+offset for x in v} for (k,v) in v.items()}
    for k,v in B.delt.items():
        delt[key_idx+k] = {k:{x+key_idx for x in v} for (k,v) in v.items()}
    B.F = {x+key_idx for x in B.F}
    pprint(delt)

    return NFA(set(delt.keys()),
        delt,
        1,
        A.F|B.F
        )

def concat_nfa(A, B):
    pprint(A.delt)
    print()
    pprint(B.delt)
    print()
    key_idx = max(A.delt.keys())+1
    delt = {}
    for k,v in A.delt.items():
        delt[k] = {k:{x for x in v} for (k,v) in v.items()}
    for s in A.F:
        try:
            delt[s][None] |= {key_idx}
        except KeyError:
            delt[s][None] = {key_idx}

    key_idx -= 1
    for k,v in B.delt.items():
        delt[key_idx+k] = {k:{x+key_idx for x in v} for (k,v) in v.items()}
    B.F = {x+key_idx for x in B.F}
    pprint(delt)

    return NFA(set(delt.keys()),
        delt,
        1,
        A.F|B.F
        )

def kleene_star(nfa):
    print()
    pprint(nfa.delt)
    delt = {1: {None : {2}}}
    for k,v in nfa.delt.items():
        delt[k+1] = {k:{x+1 for x in v} for (k,v) in v.items()}
    last_idx = len(delt.items())+2
    F = {x+1 for x in nfa.F}|{1}
    for s in F-{1}:
        try:
            delt[s][None] |= {1}
        except KeyError:
            delt[s][None] = {1}
    print()
    pprint(delt)
    print(F)

    return NFA(set(delt.keys()),
              delt,
              1,
              F)


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

    def accepted(self, string, trace=False, ret_trace=False):
        state = self.q
        output = ""
        trace_out = [state]
        output += "{}".format(state)
        for c in string:
            output += ","
            state = self.delt(state,c)
            output += "{}".format(state)
            trace_out.append(state)
        if trace:
            print(output)
        if ret_trace:
            return trace_out
        else:
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
    d_table = { str(state): { str(symbol): None for symbol in range(b) } for state in range(n) }

    d_table[None] = {None:None}
    d_table[start_s]['0'] = accept_s
    lookup = { '0': accept_s }.setdefault
    for num in range(n*b):
        num_s = num_to_baseN_str(num,b)
        end_s = str(num%n)
        before_end_state = lookup(num_s[:-1],start_s)
        d_table[before_end_state][num_s[-1]] = end_s
        lookup(num_s, end_s)

    return DFA(set(d_table.keys()),
            lambda s,c: d_table[s][c],
            '0',
            {'0'},
            set(digits))


def compile(nfa):

    Q = set()
    delt = {}
    q0 = tuple(nfa.epsilon_transition(nfa.q))
    F = set()
    sigma = nfa.sigma

    states = deque()
    states.append(q0)
    while states:

        current_states = tuple(states.popleft())
        if current_states in Q:
            continue
        
        Q.add(current_states)
        delt[current_states] = {}
        if (set(current_states) & nfa.F):
            F.add(current_states)

        for c in nfa.sigma:
            next_current_states = tuple(nfa.next_states(current_states, c))
            delt[current_states][c] = next_current_states
            states.append(next_current_states)

    return DFA(Q, lambda s,c: delt[s][c], q0, F)
