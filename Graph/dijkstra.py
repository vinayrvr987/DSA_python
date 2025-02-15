import heapq

def dijkstra(graph, src: int, n):
    dist = [float('inf')] * n
    dist[src] = 0
    min_heap = [(0, src)]

    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        if curr_dist > dist[node]:
            continue
        
        for neigbor, weight in graph[node]:
            new_dist = curr_dist + weight

            if new_dist < dist[neigbor]:
                dist[neigbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neigbor))
    return dist


if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print(dijkstra(graph, 0, 4))