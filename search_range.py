def search_range(array, target):
    start = -1
    end = -1

    for idx, i in enumerate(array):
        if i == target and start == -1:
            start = idx
        elif i == target:
            end = idx

    print(start, end)


def binary_search_range(array, query):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        if array[mid] == query and array[mid - 1] < query:
            break
        elif array[mid] < query:
            lo = mid + 1
        else:
            hi = mid - 1

    for i in range(len(array) - 1, -1, -1):
        if query == array[i]:
            return (mid, i)


nums = [1, 5, 7, 7, 7, 8, 8, 8, 8, 10]
search_range(nums, 8)
print(binary_search_range(nums, 8))
