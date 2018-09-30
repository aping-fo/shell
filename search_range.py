def search_range(array, target):
    start = -1
    end = -1

    for idx, i in enumerate(array):
        if i == target and start == -1:
            start = idx
        elif i == target:
            end = idx

    print(start, end)


nums = [5, 7, 7, 8, 8, 8, 10]
search_range(nums, 11)
