array = [1, 2, 3, 0, 4]
array1 = [1, 4, 3, 0, 2]


def garage(initial, final):
    # initial = initial[::]
    steps = 0
    seq = []

    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
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
