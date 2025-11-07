# Graph coloring using backtracking
# Graph:
# V = {0,1,2,3,4,5,6}
# E = {(0,1),(0,2),(1,3),(1,4),(2,4),(2,5),(3,6),(4,5),(4,6),(5,6)}

from typing import List, Set, Tuples

V = list(range(7))
E: Set[Tuple[int,int]] = {
    (0,1),(0,2),(1,3),(1,4),(2,4),(2,5),(3,6),(4,5),(4,6),(5,6)
}

# build adjacency list
adj = {v: set() for v in V}
for u, v in E:
    adj[u].add(v)
    adj[v].add(u)

def graph_coloring(m: int, find_all: bool = False) -> List[List[int]]:
    """
    Try to color the graph with at most m colors.
    - m: maximum number of colors (colors are integers 1..m)
    - find_all: if True, return all valid colorings; otherwise stop at first valid coloring
    Returns a list of solutions; each solution is a list `colors` where colors[i] is color of vertex i.
    """
    n = len(V)
    colors = [0] * n
    solutions: List[List[int]] = []

    def valid(vertex: int, color: int) -> bool:
        for nei in adj[vertex]:
            if colors[nei] == color:
                return False
        return True

    def backtrack(v: int = 0) -> bool:
        if v == n:
            # found a valid coloring
            solutions.append(colors.copy())
            return not find_all  # if not finding all, return True to stop early
        for c in range(1, m+1):
            if valid(v, c):
                colors[v] = c
                if backtrack(v + 1):
                    return True
                # undo
                colors[v] = 0
        return False

    backtrack(0)
    return solutions

# Example usage:
if __name__ == "__main__":
    for m in [2, 3, 4]:
        sols = graph_coloring(m, find_all=False)
        print(f"m = {m}, solutions found:", len(sols))
        if sols:
            print("example solution (vertex:color):",
                  [(i, sols[0][i]) for i in range(len(V))])
