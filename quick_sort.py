def quick_sort(arr, low, high):
    if low < high:
        n = partition(arr, low, high)
        quick_sort(arr, low, n)
        quick_sort(arr, n + 1, high)


def partition(arr, low, high):
    pivot = arr[low]

    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

        while low < high and arr[low] <= pivot:
            low += 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    arr[low] = pivot
    return low


arr = [1, 3, 2, 7, 6, 4, 5]
quick_sort(arr, 0, 6)
print(arr)
