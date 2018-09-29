def bubble(arr):
    lenght = len(arr)
    for i in range(lenght):
        for j in range(i + 1, lenght):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr)


arr = [1, 3, 2, 10, 7, 6, 4, 5]
bubble(arr)
