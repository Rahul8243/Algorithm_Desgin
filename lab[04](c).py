def first_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            high = mid - 1   # keep searching left
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

def last_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            low = mid + 1   # keep searching right
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

def count_occurrences(arr, key):
    first = first_occurrence(arr, key)
    if first == -1:   # key not found
        return 0
    last = last_occurrence(arr, key)
    return last - first + 1


# Example
arr = [2, 4, 4, 4, 7, 10]
key = 4
print("Count of", key, ":", count_occurrences(arr, key))
