import collections

'''

'''

def delete_nth_native(array, n):
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
