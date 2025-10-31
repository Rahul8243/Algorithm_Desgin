# Objective: Implement the Floyd-Warshall Algorithm to compute shortest paths between all pairs of nodes in a weighted graph.
# Problem Statement:
# You are given a directed/undirected graph with n nodes labeled 0 to n-1 and a list of edges with weights (positive or negative). Write a function:

# Floyd-Warshall Algorithm Implementation

def floyd_warshall(n, edges):
    # Step 1: Initialize the distance matrix
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    # Distance from node to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Step 2: Fill in the given edge weights
    for u, v, w in edges:
        dist[u][v] = w  # For directed graph
        # For undirected graph, also do: dist[v][u] = w

    # Step 3: Floyd–Warshall main logic
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Step 4: Detect negative cycles (optional)
    for i in range(n):
        if dist[i][i] < 0:
            print("⚠️ Graph contains a negative weight cycle!")
            break

    return dist


# -----------------------------
# Example Usage
# -----------------------------
n = 6  # nodes labeled 0 to 5
edges = [
    (0, 1, 3), 
    (1, 2, -2), 
    (2, 3, 1), 
    (0, 3, 10),
    (1, 4, -2), 
    (2, 5, 1), 
    (1, 3, -2), 
    (2, 4, 1)
]

result = floyd_warshall(n, edges)

# Print result matrix
print("Shortest distance matrix:")
for row in result:
    print(row)
