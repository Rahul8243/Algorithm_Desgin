def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Prefix sum (cumulative)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output (stable)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Example
arr3 = [4, 2, 2, 8, 3, 3, 1]
print("Counting Sort Output:", counting_sort(arr3))
