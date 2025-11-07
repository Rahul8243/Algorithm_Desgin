# Hamiltonian Cycle using Backtracking
# Graph:
# V = {0,1,2,3,4,5,6,7}
# E = {(0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,7),(6,7)}

from typing import List, Set, Tuple

# Graph Definition
V = list(range(8))
E: Set[Tuple[int, int]] = {
    (0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,7),(6,7)
}

# Build adjacency list
adj = {v: set() for v in V}
for u, v in E:
    adj[u].add(v)
    adj[v].add(u)

# Function to check if we can add a vertex to the current path
def is_valid(v: int, path: List[int], pos: int) -> bool:
    # Check adjacency
    if v not in adj[path[pos - 1]]:
        return False
    # Check if vertex is already in path
    if v in path:
        return False
    return True

def hamiltonian_cycles_util(path: List[int], pos: int, all_cycles: List[List[int]]):
    # Base case: if all vertices are included in the path
    if pos == len(V):
        # Check if last vertex connects to the first vertex
        if path[-1] in adj[path[0]]:
            all_cycles.append(path.copy())
        return

    # Try different vertices as next candidate
    for v in V[1:]:  # start from 1 (vertex 0 is fixed)
        if is_valid(v, path, pos):
            path[pos] = v
            hamiltonian_cycles_util(path, pos + 1, all_cycles)
            # backtrack
            path[pos] = -1

def find_hamiltonian_cycles() -> List[List[int]]:
    path = [-1] * len(V)
    path[0] = 0  # start at vertex 0
    all_cycles: List[List[int]] = []
    hamiltonian_cycles_util(path, 1, all_cycles)
    return all_cycles

# Run and print results
if __name__ == "__main__":
    cycles = find_hamiltonian_cycles()
    print(f"Total Hamiltonian Cycles found: {len(cycles)}\n")
    for i, cycle in enumerate(cycles, start=1):
        print(f"Cycle {i}: {cycle + [cycle[0]]}")  # close the loop
