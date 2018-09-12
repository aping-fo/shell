import collections

'''
数组展开
'''


def flatmap(array, output_arr=None):
    '''

    :param array: 输入数组
    :param output_arr: 传出数组
    :return:
    '''
    if output_arr is None:
        output_arr = []

    for ele in array:
        if isinstance(ele, collections.Iterable):
            flatmap(ele, output_arr)
        else:
            output_arr.append(ele)


array = [1, 2, 3, [4, 5, 6], 7, 8]
reslut = []

flatmap(array, output_arr=reslut)
print(reslut)
