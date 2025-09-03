def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Create buckets
    n = len(arr)
    max_val = max(arr)
    size = max_val // n + 1   # bucket range
    buckets = [[] for _ in range(n)]

    # Step 2: Distribute elements
    for num in arr:
        index = num // size
        buckets[index].append(num)

    # Step 3: Sort each bucket (Insertion Sort)
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    # Step 4: Merge buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

# Example
arr1 = [29, 25, 3, 49, 9, 37, 21, 43]
print("Bucket Sort Output:", bucket_sort(arr1))
