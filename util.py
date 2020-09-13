from collections import deque

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
