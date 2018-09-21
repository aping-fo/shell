'''
判断某位是否为0
'''


def get_bit(num, i):
    return (num & (1 << i)) != 0


print(get_bit(3, 1))


'''
设置1
'''
def set_bit(num, i):
    return num | (1 << i)


print(set_bit(3, 2))


'''
某位置0
'''
def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask

print(clear_bit(7,2))

def update_bit(num, i, bit):
    mask = ~(1 << i)
    return (num & mask) | (bit << i)
