def letter_combinations(digits):
    if digits == "":
        return []
    kmaps = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    ans = [""]
    # for c in kmaps[k]:
    #     ans.append(c)

    for num in digits:
        tmp = []
        for an in ans:
            for char in kmaps[num]:
                tmp.append(an + char)

        ans = tmp

    return ans


res = letter_combinations(['2', '9', '3'])
print(res)
