INF = float('inf')

dist = [
    [0,   3,  10, INF],
    [INF, 0,   1,   7],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
]

n = len(dist)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )

print("Shortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
