from collections import deque

def bfs(graph, src):
    n = len(graph)
    dist = [float('inf')]*n
    queue = deque([src])
    dist[src] = 0

    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight

                if weight == 0:
                    queue.appendleft((neighbor))
                else:
                    queue.append((neighbor))
    
    return dist


if __name__ == '__main__':
    graph = {
        0: [(1, 0), (3, 1)],
        1: [(3, 0), (2, 1)],
        2: [(3, 0), (5, 1)],
        3: [(4, 1)],
        4: [(5, 1), (2, 1)],
        5: []
    }
    graph2 = {
        0: [(1, 0)],
        1: [(3, 1), (2, 1)],
        2: [(3, 0), (5, 1)],
        3: [(4, 1), (0, 1)],
        4: [(5, 1), (2, 1)],
        5: []
    }
    print(bfs(graph, 0))
    print(bfs(graph2, 0))