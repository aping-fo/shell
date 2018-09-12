array = [1, 2, 3, 0, 4]
array1 = [1, 4, 3, 2, 0]


def garage(initial, final):
    # initial = initial[::]
    steps = 0
    seq = []

    '''
    算法思想
    指定一个目标值为参考
    '''
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):  # 如果参考值位置不一样，则找出目标数组值，进行交换，交换成目标数组该位置的值，然后进行下一步操作
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:  # 如果0的位置相同，则顺序找第一个不同的地方，将该位置与0进行交换，然后走上面逻辑
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        seq.append(initial[::])
        steps += 1

    return steps, seq


steps, seq = garage(array, array1)
print(seq)
print(steps)
