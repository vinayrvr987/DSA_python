from collections import deque

def hasPath(graph, src, dst):
    if src == dst: return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst): return True
    
    return False

def hasPath_bfs(graph, src, dst):
    q = deque([src])

    while q:
        node = q.popleft()
        if node == dst: return True
        for neighbor in graph[node]:
            q.append(neighbor)
    
    return False

if __name__=='__main__':
    # Testcase 1
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': ['f'],
        'f': [],
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
    print(hasPath(graph2, 'a', 'r'))
    print(hasPath(graph, 'a', 'f'))
    print(hasPath_bfs(graph2, 'a', 'r'))
    print(hasPath_bfs(graph, 'a', 'f'))