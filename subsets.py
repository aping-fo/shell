def subsets_v1(nums):
    res = [[]]

    for num in sorted(nums):
        tmp = []
        for item in res:
            tmp += [item + [num]]
        for elem in tmp:
            if elem not in res:
                res += [elem]
    return res


test = [1, 2, 3]
res = subsets_v1(test)
print(res)
