from collections import defaultdict
from collections import deque

def dfs(graph, src, dst, visited):
    visited.add(src)
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if neighbor not in visited:
            if dfs(graph, neighbor, dst, visited):
                return True
    
    return False

def bfs(graph, src, dst, visited):
    q = deque([src])
    visited.add(src)

    while q:
        node = q.popleft()
        if node == dst: return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    return False


def undirected_path(edges, src, dst):
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)
    return bfs(graph, src, dst, set())


if __name__ == '__main__':
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    print(undirected_path(edges, 'j', 'm'))
    print(undirected_path(edges, 'j', 'o'))