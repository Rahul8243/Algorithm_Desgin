import heapq

def dijkstra(V, adj, S):
    dist = [float("inf")] * V
    dist[S] = 0
    pq = [(0, S)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist


# Example Input
V, E = 5, 6
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]
S = 0

# Build adjacency list
adj = [[] for _ in range(V)]
for u, v, w in edges:
    adj[u].append((v, w))

result = dijkstra(V, adj, S)

# Output
for i in range(V):
    print(i, result[i] if result[i] != float("inf") else "INF")
