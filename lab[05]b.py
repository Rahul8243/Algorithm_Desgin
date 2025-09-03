recursive_calls = 0  # Global counter

def quicksort(arr):
    global recursive_calls
    recursive_calls += 1   # Count each call
    
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


# Example
dataset = [38, 27, 43, 3, 9, 82, 10, 16, 5, 25, 19, 72]
sorted_data = quicksort(dataset)
print("Quicksort Output:", sorted_data)
print("Total Recursive Calls:", recursive_calls)
