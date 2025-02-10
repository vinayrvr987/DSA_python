from collections import deque

def shortestPath(graph, src, dst):
    queue = deque(src)
    visited = set(src)

    length = -1
    while queue:
        size = len(queue)
        length += 1
        for _ in range(size):
            node = queue.popleft()
            if node == dst:
                return length
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return -1


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
    print(shortestPath(graph2, 'a', 'f'))
    print(shortestPath(graph2, 'a', 'd'))