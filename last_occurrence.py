def last_occurrence(array, query):
    lo, hi = 0, len(array)
    while lo <= hi:
        mid = (hi + lo) // 2
        if (array[mid] == query and mid == len(array) - 1) or \
                (array[mid] == query and array[mid + 1] > query):
            print(mid)
            return mid
        elif array[mid] <= query:
            lo = mid + 1
        else:
            hi = mid - 1


arr = [0, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8]
print(last_occurrence(arr, 6))
