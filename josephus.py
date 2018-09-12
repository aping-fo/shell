def josephus(int_list, skip):
    idx = 0
    skip = skip

    skiptmp = 0
    while len(int_list) > 0:
        if idx >= len(int_list):
            idx = 0

        flag = False
        if skiptmp == skip - 1:
            ele = int_list.pop(idx)
            print(ele)
            skiptmp = 0
            idx -= 1  # 有删除回退一位
            flag = True

        idx += 1
        skiptmp += 1

        if flag:  # 有删除回退一位
            skiptmp -= 1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
josephus(array, 3)
