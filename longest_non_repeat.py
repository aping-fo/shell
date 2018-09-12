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


longest_non_repeat_v1('abcabcbbcdef')
