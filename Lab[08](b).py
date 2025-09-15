def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX, rootY = find(parent, x), find(parent, y)
    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True
    return False

def kruskal(N, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    mst = []
    total_edges = 0

    for u, v, w in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, w))
            total_edges += 1

    if total_edges != N-1:
        return None
    return mst


# Example Input
N, M = 4, 5
edges = [
    (1, 2, 10),
    (1, 3, 6),
    (1, 4, 5),
    (2, 4, 15),
    (3, 4, 4)
]

mst = kruskal(N, edges)

if mst is None:
    print("The graph is not fully connected.")
else:
    print("Minimum Spanning Tree edges:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
