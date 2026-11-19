def kruskal(vertex, edge):
    edge.sort(key=lambda edge: edge[2])

    graph = [[v] for v in vertex]
    mst = []
    cost = 0

    for i, j, weight in edge:
        grp_i = None
        grp_j = None

        for g in graph:
            if i in g:
                grp_i = g
            if j in g:
                grp_j = g

        if grp_i != grp_j:
            mst.append((i, j, weight))
            cost += weight

            new_group = grp_i + grp_j
            graph.remove(grp_i)
            graph.remove(grp_j)
            graph.append(new_group)

        if len(mst) == len(vertex) - 1:
            break

    if len(mst) != len(vertex) - 1:
        print("Graph is not connected!")
        return

    print("Minimum Spanning Tree:")
    for i, j, weight in mst:
        print(i, "-", j, ":", weight)

    print("Total Minimum Cost:", cost)# User input
vertex = list(map(int, input("Enter vertices: ").split()))
e = int(input("Enter number of edges: "))

edge = []
print("Enter edges as: source destination weight")

for _ in range(e):
    i, j, weight = map(int, input().split())
    edge.append((i, j, weight))

kruskal(vertex, edge)
