def limit(arr, min=None, max=None):
    result = []

    for i in arr:

        if min is None:
            if i <= max:
                result.append(i)

        elif max is None:
            if i >= min:
                result.append(i)
        else:
            if min <= i <= max:
                result.append(i)

    return result


array = [1, 2, 3, 4, 5]
result1 = limit(array, max=3)
print(result1)
