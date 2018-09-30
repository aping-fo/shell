def search_insert(array, val):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if val > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


array = [1, 3, 5, 6]
print(search_insert(array, 7))
