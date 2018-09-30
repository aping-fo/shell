def find_min_rotate(array):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (low + high) // 2
        if array[mid] > array[high]:
            low = mid + 1
        else:
            high = mid

    return array[low]


arr = [4, 5, 6, 7, 8, 0, 1, 2, 3]
print(find_min_rotate(arr))
