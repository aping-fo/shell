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


def subsets_v2(nums):
    def backtrack(res, nums, stack, pos):
        if pos == len(nums):
            res.add(tuple(stack))
        else:
            stack.append(nums[pos])
            backtrack(res, nums, stack, pos + 1)
            stack.pop()
            backtrack(res, nums, stack, pos + 1)

    res = set()
    backtrack(res, nums, [], 0)
    print(list(res))


test = [1, 2, 3]
res = subsets_v1(test)
print(res)

test1 = [1,2]
subsets_v2(test1)
