def find_triplet_element(arr):
    for num in set(arr):   # check unique elements
        if arr.count(num) == 3:
            return num
    return None

# Example
arr = [4, 5, 4, 3, 5, 7, 3, 3, 15]
print("Element occurring 3 times:", find_triplet_element(arr))
