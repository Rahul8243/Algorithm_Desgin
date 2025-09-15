import heapq

def prim_mst(N, edges):
    adj = [[] for _ in range(N)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))
    
    visited = [False] * N
    min_heap = [(0, 0)]  # (cost, node)
    total_cost = 0
    count = 0
    
    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        count += 1
        
        for w, v in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    
    if count == N:
        return total_cost
    else:
        return "Network is disconnected"

# Example Input
N, M = 4, 5
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print(prim_mst(N, edges))  # Output: 19
