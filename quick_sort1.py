def quick_sort(arr, low, high):
    pivot = arr[low]
    l = low
    h = high

    while l < h:
        while l < h and arr[h] >= pivot:
            h -= 1
        if l < h:
            arr[l] = arr[h]
            l -= 1

        while l < h and arr[l] < pivot:
            l += 1
        if l < h:
            arr[h] = arr[l]
            h -= 1

    arr[l] = pivot

    if low < l - 1:
        quick_sort(arr, low, l - 1)
    if l + 1 < high:
        quick_sort(arr, h + 1, high)


arr = [1, 3, 2, 10, 7, 6, 4, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
