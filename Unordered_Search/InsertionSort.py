#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
插入排序
"""


def insertionSort(alist):
    for index in range(1, len(alist)):
        # 新项/插入项
        currentvalue = alist[index]
        position = index
        while position > 0 and currentvalue < alist[position-1]:
            # 比对、移动
            alist[position] = alist[position-1]
            position -= 1
        # 插入新项
        alist[position] = currentvalue


alist = [89, 67, 56, 45, 34, 23, 1]
insertionSort(alist)
print(alist)
