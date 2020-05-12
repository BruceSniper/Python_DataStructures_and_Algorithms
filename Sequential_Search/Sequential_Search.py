#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang


def sequentialSearch(alist, item):
    pos = 0
    found = False
    position = None

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
            position = pos
        else:
            # 下标顺序增长
            pos += 1
    return found, position


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))
