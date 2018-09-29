def shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            j = i

            while j - gap > 0 and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap = gap // 2

    print(arr)


arr = [1, 3, 2, 10, 7, 6, 4, 5]
shell_sort(arr)
