def prim(graph, n):
    visited = [False] * n
    visited[0] = True

    edges = []
    total_cost = 0

    for _ in range(n - 1):
        min_cost = float('inf')
        u = -1
        v = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < min_cost:
                            min_cost = graph[i][j]
                            u = i
                            v = j

        if u == -1:
            print("Graph is not connected!")
            return

        edges.append((u, v, min_cost))
        total_cost += min_cost
        visited[v] = True

    print("\nMinimum Spanning Tree:")
    for u, v, cost in edges:
        print(u, "-", v, ":", cost)

    print("Total Minimum Cost:", total_cost)



n = int(input("Enter number of vertices: "))
graph = [[0] * n for _ in range(n)]

e = int(input("Enter number of edges: "))

print("Enter edges as: source destination weight")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

prim(graph, n)
