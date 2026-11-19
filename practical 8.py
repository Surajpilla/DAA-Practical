#bfs
from collections import deque

def bfs(adj):
    n = len(adj)
    visited = [False] * n
    res = []

    src = 0
    g = deque()

    g.append(src)
    visited[src] = True
    while g:
        u = g.popleft()
        res.append(u)

        for v in adj[u]:
            if not visited[v]:
                g.append(v)
                visited[v] = True

    return res

adj = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2, 4],
    [3]
]

print("BFS Traversal:", bfs(adj))




#DFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(neighbour)

print("DFS Traversal:")
dfs('A')
