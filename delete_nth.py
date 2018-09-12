import collections

'''
从一个数组中，选择出现小于等于目标次数的元素

列如：
input array = [1,2,3,1,2,1,2,3]，元素可重复次数是2
output result = [1,2,3,1,2,3]
'''


def delete_nth_native(array, n):
    '''

    :param array: 目标数组
    :param n: 元素可重复次数
    :return: 返回一个结果数组
    '''
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)

    return ans


def delete_nth(array, n):
    ans = []
    counter = collections.defaultdict(int)

    for i in array:
        if counter[i] < n:
            ans.append(i)
            counter[i] += 1

    return ans


test = [1, 2, 3, 1, 2, 1, 2, 3]

result = delete_nth_native(test, 2)
print(result)

print(delete_nth(test, 2))
