def two_sum(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target - num in dic:
            return [dic[target - num] + 1, i + 1]
        dic[num] = i


numbers = [2, 4, 7, 11, 15]
target = 9

print(two_sum(numbers, target))
