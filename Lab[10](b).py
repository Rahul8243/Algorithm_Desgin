import time

# 1. Naive Recursive Solution
def binomial_recursive(n, r):
    if r == 0 or r == n:
        return 1
    return binomial_recursive(n-1, r-1) + binomial_recursive(n-1, r)

# 2. Top-Down DP with Memoization
def binomial_top_down(n, r, memo=None):
    if memo is None:
        memo = {}
    if r == 0 or r == n:
        return 1
    if (n, r) in memo:
        return memo[(n, r)]
    memo[(n, r)] = binomial_top_down(n-1, r-1, memo) + binomial_top_down(n-1, r, memo)
    return memo[(n, r)]

# 3. Bottom-Up DP with Tabulation (Space-Optimized)
def binomial_bottom_up(n, r):
    if r > n - r:  # Use symmetry property
        r = n - r
    C = [0] * (r+1)
    C[0] = 1  # C(n, 0) = 1

    for i in range(1, n+1):
        # Compute next row using previous row from right to left
        j = min(i, r)
        while j > 0:
            C[j] = C[j] + C[j-1]
            j -= 1
    return C[r]

# Function to run tests and measure time
def test_binomial(n, r):
    print(f"\nComputing C({n},{r}):")
    
    # Recursive
    start = time.time()
    rec_res = binomial_recursive(n, r)
    end = time.time()
    print(f"Naive Recursive: {rec_res} (Time: {end-start:.6f} sec)")

    # Top-down
    start = time.time()
    td_res = binomial_top_down(n, r)
    end = time.time()
    print(f"Top-Down DP: {td_res} (Time: {end-start:.6f} sec)")

    # Bottom-up
    start = time.time()
    bu_res = binomial_bottom_up(n, r)
    end = time.time()
    print(f"Bottom-Up DP (Space-Optimized): {bu_res} (Time: {end-start:.6f} sec)")

# Small examples
test_binomial(5, 2)
test_binomial(6, 3)

# Large examples
test_binomial(50, 25)
test_binomial(100, 50)
