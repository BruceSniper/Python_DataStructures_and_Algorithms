#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    position = None
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
            position = pos
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found, position


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))
