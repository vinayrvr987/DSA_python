def dfs(graph, src, visited):
    if src in visited:
        return 0
    visited.add(src)
    size = 1
    for neighbor in graph[src]:
        size += dfs(graph, neighbor, visited)
    return size



def largestComponent(graph):
    max_length = 0
    visited = set()
    for node in graph:
        current_length = dfs(graph, node, visited)
        max_length = max(current_length, max_length)
    return max_length

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
        'j': [],
        'z': []
    }
    print(largestComponent(graph2))