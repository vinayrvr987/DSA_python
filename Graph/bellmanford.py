from collections import deque

def bellmanford_dp(graph, src, n):
    dist = [float('inf')] * n
    queue = deque([src])
    dist[src] = 0

    while queue:
        node = queue.popleft()
        for neighbor, wt in graph[node]:
            if dist[node] + wt < dist[neighbor]:
                dist[neighbor] = dist[node] + wt
                queue.append(neighbor)
    
    for i in range(n):
        if dist[i] == float('inf'):
            dist[i] = -1
    
    return dist


if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print(bellmanford_dp(graph, 0, 4))