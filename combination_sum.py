'''

给出指定数组 和指定 目标值

求出所有组合和等于目标值

'''

import itertools

"""
利用Python 的API来计算
(组合可以重复)

"""


def combination_sum1(arr, target):
    res = []
    lenght = len(arr)
    for size in range(1, lenght):
        for i in itertools.combinations_with_replacement(arr, size):  # 全排列，可以重组自己
            s = sum(i)
            if s == target:
                res.append(list(i))
    return res


"""
利用Python 的API来计算
(组合)

"""


def combination_sum2(arr, target):
    res = []
    lenght = len(arr)
    for size in range(1, lenght):
        for i in itertools.combinations(arr, size):  # 组合，不可重组自己
            s = sum(i)
            if s == target:
                  res.append(i)
    return res


arr = [2, 3, 6, 7]
res = combination_sum1(arr, 7)
res1 = combination_sum2(arr, 7)
print(res1)
print(res)
