def rotate_1(array, k):
    lenght = len(array)
    k = k % lenght

    reslut = array[lenght - k:] + array[: lenght - k]

    print(reslut)


array = [1, 2, 3, 4, 5, 6, 7]
k = 13

rotate_1(array, k)
