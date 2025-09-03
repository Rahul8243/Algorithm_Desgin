def second_smallest(arr):
    if len(arr) < 2:
        return None

    if arr[0] < arr[1]:
        first_smallest_num = arr[0]
        second_smallest_num = arr[1]
    else:
        first_smallest_num = arr[1]
        second_smallest_num = arr[0]

    for i in range(2, len(arr)):
        if arr[i] < first_smallest_num:
            second_smallest_num = first_smallest_num
            first_smallest_num = arr[i]
        elif first_smallest_num < arr[i] < second_smallest_num:
            second_smallest_num= arr[i]

    return second_smallest_num


arr = [5, 2, 8, 1, 3]
print(second_smallest(arr)) 
