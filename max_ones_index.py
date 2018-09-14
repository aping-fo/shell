def max_ones_index(array):
    max_len = 0
    zero_count = 0
    zero_pre = 0
    zero_after = 0

    for i in array:
        if i == 1:
            zero_pre += 1
        elif i == 0:
            zero_count += 1
            zero_after = zero_pre
            zero_pre = 0
            if zero_count == 2:
                max_len = max(max_len, zero_after + zero_pre + 1)
                zero_count = 0
    max_len = max(max_len, zero_after + zero_pre + 1)
    print(max_len)


array = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
max_ones_index(array)
