def selection_sort(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[min], arr[i] = arr[i], arr[min]

    print(arr)


arr = [1, 3, 2, 10, 7, 6, 4, 5]
selection_sort(arr)
