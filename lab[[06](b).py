def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9

    # Count digits
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Prefix sum (cumulative count)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output (stable)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy back
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Example 1
arr2 = [170, 45, 75, 90, 802, 24, 2, 66]
print("Radix Sort Output:", radix_sort(arr2))
