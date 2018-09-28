def quick_sort(arr, low, high):
    if low < high:
        n = partition(arr, low, high)
        quick_sort(arr, low, n - 1)
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


arr = [1, 3, 2, 10, 7, 6, 4, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
