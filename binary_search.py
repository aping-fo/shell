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


def binary_search_recur(array, query, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    midVal = array[mid]
    if query == midVal:
        return mid
    elif query > midVal:
        return binary_search_recur(array, query, mid + 1, high)
    else:
        return binary_search_recur(array, query, low, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = binary_search(arr, 10)

print(ret)
ret = binary_search_recur(arr, 10, 0, 9)
print(ret)
