# DSA Python

This repository contains various data structures and algorithms implemented in Python.

## Graph Algorithms

### Depth-First Search (DFS) and Breadth-First Search (BFS)

#### File: `Graph/problems/hasPath.py`

This file contains functions to determine if there is a path between two nodes in a graph using both DFS and BFS.

- `hasPath(graph, src, dst)`: Uses DFS to check if there is a path from `src` to `dst`.
- `hasPath_bfs(graph, src, dst)`: Uses BFS to check if there is a path from `src` to `dst`.

#### File: `Graph/bfs.py`

This file contains functions to perform BFS on a graph.

- `bfs(graph, source, visited=None)`: Performs BFS starting from the `source` node and prints each visited node.
- `bfs_all(graph)`: Performs BFS for all nodes in the graph, ensuring all components are covered.

#### File: `Graph/problems/undirectedPath.py`

This file contains functions to determine if there is a path between two nodes in an undirected graph using both DFS and BFS.

- `dfs(graph, src, dst, visited)`: Uses DFS to check if there is a path from `src` to `dst`.
- `bfs(graph, src, dst, visited)`: Uses BFS to check if there is a path from `src` to `dst`.
- `undirected_path(edges, src, dst)`: Builds the graph from the given edges and uses BFS to check if there is a path from `src` to `dst`.
