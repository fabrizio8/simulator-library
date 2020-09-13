from collections import deque

def gen_graph(dfa):
    graph = {}
    for state in dfa.Q:
        try:
            graph[state] = list({dfa.delt(state, c) for c in dfa.sigma})
        except:
            print(dfa)
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

def find_accepted_string(dfa):
    # no accepted states, won't find an acceptable string
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
