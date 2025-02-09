from collections import deque

def bfs(graph, source, visited=None):
    q = deque([source])
    visited.add(source)
    while q:
        node = q.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

def bfs_all(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)

if __name__ == '__main__':
    # Testcase 1
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
        'r': ['j'],
        'j': []
    }
    # Testcase 2
    graph2 = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': ['f'],
        'f': [],
        'r': ['j'],
        'j': []
    }
    bfs_all(graph2)
    bfs(graph2, 'a', set())