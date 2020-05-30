#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
冒泡排序，时间复杂度O(n^2)
"""


def bubbleSort(alist):
    # n-1趟
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                """
                序错，交换
                在python中，可以直接交换：
                alist[i], alist[i+1] = alist[i+1], alist[i]
                """
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


alist = [54, 26, 93, 17, 77, 31, 44, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)
