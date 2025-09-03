def search_rotated(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1  # key not found


# Example
arr = [13, 18, 25, 2, 8, 10]
key = 8
print("Index of", key, ":", search_rotated(arr, key))
