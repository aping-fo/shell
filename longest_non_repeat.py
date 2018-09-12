import collections


def longest_non_repeat_v1(str1):
    tmpdic = dict()
    beginIdx = 0
    endIdx = 0
    len = 0

    max_begin_idx = 0
    max_end_idx = 0
    maxlen = 0

    for s in str1:
        if tmpdic.get(s) is None:
            tmpdic[s] = s
            endIdx += 1
            len += 1
        else:
            if maxlen < len:
                max_begin_idx = beginIdx
                max_end_idx = endIdx
                maxlen = len
            tmpdic.clear()
            tmpdic[s] = s
            len = 1
            beginIdx = endIdx
            endIdx += 1

    if maxlen < len:
        max_begin_idx = beginIdx
        max_end_idx = endIdx
        maxlen = len
    print(str1[max_begin_idx:max_end_idx])


def longest_non_repeat_v2(string):
    """
    Apply slide windown.
    """
    dict = {}  # 记录每个字符最后出现位置
    max_length = 0
    j = 0
    for i in range(len(string)):
        if string[i] in dict:
            j = max(dict[string[i]], j)  # 最后一个重复出现的字符位置
        dict[string[i]] = i + 1
        max_length = max(max_length, i - j + 1)
    print(max_length)


longest_non_repeat_v1('abcabcbbcdef')
longest_non_repeat_v2('abcabcbbcdef')
