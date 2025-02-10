def dfs(graph, src, visited):
    if src is None:
        return
    if src not in visited:
        visited.add(src)
        for neighbor in graph[src]:
            dfs(graph, neighbor, visited)
    return


def connectedComponents(graph):
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            count += 1
            dfs(graph, node, visited)
    return count


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
    print(connectedComponents(graph2))