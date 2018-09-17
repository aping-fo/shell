def move_zeros_toend(array):
    result = []
    zeros = 0
    for i in array:
        if i == 0:
            zeros += 1
        else:
            result.append(i)

    result.extend([0] * zeros)
    print(result)


array = [False, 1, 0, 1, 2, 0, 1, 3, "a"]

move_zeros_toend(array)
