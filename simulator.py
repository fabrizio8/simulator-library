from random import randint
from typing import Callable, Dict
from collections import deque
from itertools import combinations

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


def gen_graph(dfa, sigma):
    graph = {}
    for state in dfa.Q:
        graph[state] = list({dfa.delt(state, c) for c in sigma})
    return graph


def bfs(graph, start, end):
    queue = deque()
    queue.append([start])
    visited = set()

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == end:
            return path
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            visited.add(vertex)


def find_accepted_string(dfa, sigma):
    # no accepted states, won't find an acceptable string
    if not dfa.F:
        return None
    graph = gen_graph(dfa, sigma)
    path = []
    for accepting in dfa.F:
        if path:
            break
        path = bfs(graph, dfa.q, accepting)
    string = []
    for idx, node in enumerate(path[:-1]):
        for c in sigma:
            if dfa.delt(path[idx],c) == path[idx+1]:
                string.append(c)
                break
    print('res', string)
    return string

