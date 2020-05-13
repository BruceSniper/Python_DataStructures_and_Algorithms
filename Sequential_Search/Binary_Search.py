#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
二分查找，复杂度O(log n)
"""


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

"""
使用递归的二分查找
"""
def binarySearchUsingRecursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            # 缩小规模
            if item < alist[midpoint]:
                # 调用自身
                return binarySearchUsingRecursion(alist[:midpoint], item)
            else:
                return binarySearchUsingRecursion(alist[midpoint+1:], item)