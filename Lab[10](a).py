def knapsack(weights, values, W):
    n = len(weights)
    
    # DP table
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Maximum value
    max_value = dp[n][W]

    # Trace back to find selected items
    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i)   # 1-based index
            w -= weights[i-1]

    selected_items.reverse()
    return max_value, selected_items


# -------- Main Program --------
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    W = int(input("Enter capacity of knapsack: "))

    weights = []
    values = []
    print("Enter weight and value of each item:")
    for _ in range(n):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)

    max_val, items = knapsack(weights, values, W)

    print("Maximum value achievable:", max_val)
    print("Selected items (1-based index):", items)
