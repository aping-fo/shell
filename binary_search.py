def binary_search(array, query):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1

    return None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = binary_search(arr, 10)

print(ret)
