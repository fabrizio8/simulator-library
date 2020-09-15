from collections import deque
from string import ascii_uppercase, digits
import pdb

def gen_graph(dfa):
    graph = {}
    for state in dfa.Q:
        try:
            graph[state] = list({dfa.delt(state, c) for c in dfa.sigma})
        except Exception as e:
            print(e)
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
            for current_neighbour in graph.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            visited.add(vertex)

def find_accepted_string(dfa):

    if not dfa.F:
        return None
    graph = gen_graph(dfa)
    path = []
    for accepting in dfa.F:
        if path:
            break
        path = bfs(graph, dfa.q, accepting)
    string = []
    if not path:
        return None
    for idx, node in enumerate(path[:-1]):
        for c in dfa.sigma:
            if dfa.delt(path[idx],c) == path[idx+1]:
                string.append(c)
                break
    return string


def try_delta(f,*args):
  try:
    return f(*args)
  except:
    return None


def num_to_baseN_str(n, b, syms=digits+ascii_uppercase):
    return ((n == 0) and syms[0]) or (num_to_baseN_str(n//b, b, syms).lstrip(syms[0]) + syms[n % b])
