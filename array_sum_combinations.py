def array_sum_combinations(A, B, C, target):
    def over(constructed_sofar):
        sum = 0
        to_stop, reached_target = False, False
        for elem in constructed_sofar:
            sum += elem
        if sum >= target and len(constructed_sofar) >= 3:
            to_stop = True
            if sum == target and 3 == len(constructed_sofar):
                reached_target = True

        return to_stop, reached_target

    def construct_candidates(constructed_sofar):
        array = A
        if 1 == len(constructed_sofar):
            array = B
        elif 2 == len(constructed_sofar):
            array = C
        return array

    def backtrack(constructed_sofar=[], res=[]):
        to_stop, reached_target = over(constructed_sofar)
        if to_stop:
            if reached_target:
                res.append(constructed_sofar)
            return
        candidates = construct_candidates(constructed_sofar)

        for candidate in candidates:
            constructed_sofar.append(candidate)
            backtrack(constructed_sofar[:], res)
            constructed_sofar.pop()

    res = []
    backtrack([], res)
    return res


A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [2, 3, 3, 4]
target = 7

res = array_sum_combinations(A, B, C, target)
print(res)
