def fractional_knapsack(n, items, W):
    # Sort by value-to-weight ratio (descending)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_value = 0.0
    for weight, value in items:
        if W == 0:
            break
        if weight <= W:
            total_value += value
            W -= weight
        else:
            total_value += value * (W / weight)
            W = 0
    return round(total_value, 2)

n = 3
items = [(10, 60), (20, 100), (30, 120)]
W = 50

print(fractional_knapsack(n, items, W))  
