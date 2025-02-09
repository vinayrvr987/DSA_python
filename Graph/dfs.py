# Description: Depth First Search Algorithm
def dfs(graph, source=None, visited=None):
    if source is None:
        return
    if source not in visited:
        print(source)
        visited.add(source)
        for neighbor in graph[source]:
            dfs(graph, neighbor, visited)
    return

def dfs_all(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)

if __name__ == '__main__':
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
    dfs_all(graph2)
    dfs(graph, 'a', set())